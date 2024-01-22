#! /usr/bin/env python
import os
import json
import argparse
from dotenv import load_dotenv
from Models.Gpt import Gpt
from Models.Api import Api
from Models.DalleOpenAi import DalleOpenAi
from Models.RoleSelector import RoleSelector
from Models.StableDiffusion import StableDiffusion
from Models.Social.Twitter import Twitter
from Models.Social.Telegram import Telegram
from Models.Social.Mastodon import Mastodon
#from Models.Social.Instagram import Instagram
import asyncio

load_dotenv()

DEBUG = os.getenv("DEBUG")
API_UPLOAD = os.getenv("API_UPLOAD")
TWITTER_AUTO_PUBLISH = os.getenv("TWITTER_AUTO_PUBLISH")
TELEGRAM_AUTO_PUBLISH = os.getenv("TELEGRAM_AUTO_PUBLISH")
MASTODON_AUTO_PUBLISH = os.getenv("MASTODON_AUTO_PUBLISH")
# INSTAGRAM_AUTO_PUBLISH = os.getenv("INSTAGRAM_AUTO_PUBLISH")

## Preparo parámetros recibidos por consola
parser = argparse.ArgumentParser(description="Tool for prompt generator and stable diffusion images creator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--only-prompts", action="store_true", help="Indica que solo vas a generar prompts y volcarlos a un archivo CSV en modo listado")
parser.add_argument("--output-path", default="output", help="Ruta donde se van a guardar los archivos generados")
parser.add_argument("--stable-diffusion", action="store_true", help="Usa la API de Stable Diffusion")
parser.add_argument("--dalle", action="store_true", help="Usa la API de Dall-e")
parser.add_argument("quantity", type=int, help="Cantidad a generar (imágenes o prompts)")
parser.add_argument("size", default="128x128", nargs='?', help="Cantidad a generar (imágenes o prompts)")
args = parser.parse_args()
config = vars(args)

if DEBUG:
    print("")
    print("")
    print("Parámetros recibidos por consola:", config)
    print("")

OUTPUT_PATH = config['output_path']

## Establezco variables de configuración
quantity = config['quantity']
only_prompts = config['only_prompts']
stable_diffusion = config['stable_diffusion']
dalle = config['dalle']
size = config['size']

## Instancia del role
role = RoleSelector()

## Instancia para comunicarse con la API de GPT
gpt = Gpt(role)

## Si solo vamos a generar un listado de prompts en csv
if only_prompts:
    print("")
    print("Generando listado de prompts a CSV")
    print("")

    gpt.generate_prompts_to_csv(quantity=quantity)

    ## Añado evento al log histórico
    with open("historical.log", "a") as file:
        file.write(f"\nSe han generado {quantity} prompts desde la api GPT al archivo CSV")

    exit(0)

## Pide a la API un nuevo prompt
promptDict = gpt.next_prompt()

"""
promptDict = {
    "title": "Warrior night elf from world of Warcraft",
    "description": "A 3d digital image Sylvanas Windrunner character of world of warcraft",
    "metatags": "wow, world of warcraft, night elf, digital",
    "prompt": "Warrior night elf from world of Warcraft woorigami a beautiful and strong purple female warrior night elf, world of warcraft, character concept art of an anime goddess of lemons | | cute - fine - face, pretty face, realistic shaded perfect face, fine details by stanley artgerm lau, wlop, rossdraws, james jean, andrei riabovitchev, marc simonetti, boris valejo, frank franzetta, and sakimichan, trending on artstation, folded, paper-made, origami , (Masterpiece:1. 3) (best quality:1. 2) (high quality:1. 1), intricate detail, vivid details, awe inspiring"
}
promptDict = {
    "title": "World of warcraft elven druid",
    "description": "fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski",
    "metatags": "wow, world of warcraft, night elf, digital",
    "prompt": "world of warcraft elven druid, fantasy, intricate, elegant,highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski, wow, world of warcraft, night elf, digital"
}

role.change_role('art_3d_people')
"""


if not isinstance(promptDict, dict) or not promptDict['prompt']:
    print("Error al obtener el prompt")

    exit(1)

prompt = promptDict['prompt']
title = promptDict['title']
description = promptDict['description']
metatags = promptDict['metatags']

if stable_diffusion:
    stable_diffusion = StableDiffusion(gpt.role, debug=DEBUG)
    path = stable_diffusion.generate_images(prompt=prompt, quantity=quantity, size=size, path=title)
    seeds = stable_diffusion.get_seeds()
    params = stable_diffusion.get_params()
    ai = "Stable Diffusion"
elif dalle:
    ## Instancia del modelo para Dall-e
    apiModel = DalleOpenAi(model="davinci", debug=DEBUG)

    ## Genera una imagen desde la api de Dall-e
    path = apiModel.generate_images(prompt, quantity, size, title)
    seeds = []
    params = {}
    ai = "Dall-e"
else:
    ai = ""
    params = {}

# Separo los metatags en una lista
metatagsList = metatags.split(",")
metatagsList = [x.strip() for x in metatagsList]

## Creo una cadena con los hashtags (# + nombre del tag)
hashtagsList = [f"#{x}" for x in metatagsList]
hashtags = ", ".join(hashtagsList)

# Uno los seed en una cadena
seedsString = ", ".join(str(x) for x in seeds)

## Información para archivo JSON
jsonInfo = {
    "batch_id": os.urandom(16).hex(), # Genero un ID aleatorio para el archivo JSON, con esto se puede identificar para asociar luego vídeo tras subir a mi web api y youtube
    "ai": ai,
    "role": role.role,
    "title": title,
    "description": description,
    "tags": metatagsList,
    "prompt": prompt,
    "size": size,
    "quantity": quantity,
    "model": params.get("model", "Does not apply"),
    "steps": params.get("steps", "Does not apply"),
    "cfg_scale": params.get("cfg_scale", "Does not apply"),
    "denoising_strength": params.get("denoising_strength", "Does not apply"),
    "sampler_index": params.get("sampler_index", "Does not apply"),
    "restore_faces": params.get("restore_faces", "Does not apply"),
    "negative_prompt": params.get("negative_prompt", "Does not apply"),
    "seeds": seeds,
    "resizer": "Real-ESRGAN x4",
    "refiner_model": "sd_xl_refiner_1.0_f16.ckpt",
}

## Mezclo el archivo JSON con los parámetros de configuración
jsonInfo.update(params)

## Información para archivo markdown
stringInfoMd = f"\nAI: {ai}\nTitle: {title}\nNumber of images: {quantity}\n\n## Prompt\n\n{prompt}\n\n## Tags\n\n{metatags}\n\n{hashtags}\n\n## Settings\n\nModel: {params.get('model', 'Does not apply')}\nSize: {size}\nSteps: {params.get('steps', 'Does not apply')}\nCfg Scale: {jsonInfo.get('cfg_scale')}\nDenoising Strength: {jsonInfo.get('denoising_strength')}\nSampler Index: {jsonInfo.get('sampler_index')}\nRestore Faces: {jsonInfo.get('restore_faces')}\n\n## Negative Prompt\n\n{jsonInfo.get('negative_prompt')}\n\n## Seeds (in order)\n\n{seedsString}\n"

infoMdFile = path + "/info.md"
infoJsFile = path + "/info.json"

## Ruta al archivo oculto indicando que todas las imágenes fueron generadas
imagesGeneratedFile = path + "/.all_images_generated"

## Almaceno los datos en markdown
with open(infoMdFile, "w") as file:
    file.write(stringInfoMd)

## Almaceno los datos en json
with open(infoJsFile, "w") as file:
    file.write(json.dumps(jsonInfo))

## Archivo oculto indicando que todas las imágenes fueron generadas
with open(imagesGeneratedFile, "w") as file:
    file.write(f"Images Generated: {quantity}")

## Añado evento al log histórico
with open("historical.log", "a") as file:
    file.write(f"\nSe han generado {quantity} imágenes desde la api {ai} con el prompt: {prompt}")

api_response = None

## Postear en mi web
if API_UPLOAD:
    api = Api()
    api_response = api.directoryUpload(jsonInfo, path)

web_link = api_response.get('url') if api_response else None

## Postear en twitter
if TWITTER_AUTO_PUBLISH:
    print("Compartiendo imágenes en publicación de Twitter...")
    twitter = Twitter()
    twitter.post_tweet(jsonInfo=jsonInfo, path=path, link=web_link, max_images=3)

## Postear en Canal de Telegram
if TELEGRAM_AUTO_PUBLISH:
    print("Compartiendo imágenes en publicación de Telegram...")
    telegram = Telegram()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(telegram.publish(jsonInfo=jsonInfo, path=path, max_images=3, link=web_link))

if MASTODON_AUTO_PUBLISH:
    print("Compartiendo imágenes en publicación de Mastodon...")
    mastodon = Mastodon()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(mastodon.publish(jsonInfo=jsonInfo, path=path, max_images=3, link=web_link))


## Postear en Instagram
# if INSTAGRAM_AUTO_PUBLISH:
#     print("Compartiendo imágenes en publicación de Instagram...")
#     instagram = Instagram()
#     instagram.publish(jsonInfo=jsonInfo, path=path)


## Muevo la colección hacia el directorio final
if OUTPUT_PATH != 'output':
    os.rename(path, OUTPUT_PATH + "/" + jsonInfo.get('batch_id') + " - " + title)


exit(0)
