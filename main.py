#! /usr/bin/env python
import os
from dotenv import load_dotenv
import argparse
from Models.DalleOpenAi import DalleOpenAi
from Models.Gpt import Gpt
from Models.StableDiffusion import StableDiffusion
import json

load_dotenv()

DEBUG = os.getenv("DEBUG")

## Preparo parámetros recibidos por consola
parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--only-prompts", action="store_true", help="Indica que solo vas a generar prompts y volcarlos a un archivo CSV en modo listado")
parser.add_argument("--stable-diffusion", action="store_true", help="Usa la API de Stable Diffusion")
parser.add_argument("--dalle", action="store_true", help="Usa la API de Dall-e")
parser.add_argument("quantity", type=int, help="Cantidad a generar (imágenes o prompts)")
parser.add_argument("size", default="128x128", nargs='?', help="Cantidad a generar (imágenes o prompts)")
args = parser.parse_args()
config = vars(args)

if DEBUG:
    print("")
    print("Parámetros recibidos:", config)
    print("")

## Establezco variables de configuración
quantity = config['quantity']
only_prompts = config['only_prompts']
stable_diffusion = config['stable_diffusion']
dalle = config['dalle']
size = config['size']

## Instancia para comunicarse con la API de GPT
gpt = Gpt()

## Si solo vamos a generar un listado de prompts en csv
if only_prompts:
    print("")
    print("Generando listado de prompts a CSV")
    print("")

    gpt.generate_prompts_to_csv(quantity=quantity)

    exit(0)

## Pide a la API un nuevo prompt
promptDict = gpt.next_prompt()

if not isinstance(promptDict, dict) or not promptDict['prompt']:
    print("Error al obtener el prompt")

    exit(1)

prompt = promptDict['prompt']
title = promptDict['title']
description = promptDict['description']
metatags = promptDict['metatags']
steps=10

if stable_diffusion:
    stable_diffusion = StableDiffusion(debug=DEBUG)
    path = stable_diffusion.generate_images(prompt=prompt, quantity=quantity, size=size, path=title, steps=steps)

elif dalle:
    ## Instancia del modelo para Dall-e
    apiModel = DalleOpenAi(model="davinci", debug=DEBUG)

    ## Genera una imagen desde la api de Dall-e
    path = apiModel.generate_images(prompt, quantity, size, title)


## Información para archivo markdown
stringInfoMd = f"# Info\n\nTitle: {title}\nCantidad de imágenes: {quantity}\n\n## Descripción de la búsqueda\n\n{prompt}\n\n## Etiquetas\n\n{metatags}\n\n# Parámetros de configuración\n\nTamaño: {size}\nPasos: {steps}\n"

# Separo los metatags en una lista
metatagsList = metatags.split(",")

metatagsList = [x.strip() for x in metatagsList]

## Información para archivo JSON
jsonInfo = {
    "title": title,
    "description": description,
    "metatags": metatagsList,
    "size": size,
    "steps": steps,
    "prompt": prompt,
    "quantity": quantity,
}

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

exit(0)
