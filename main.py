#! /usr/bin/env python
import os
from dotenv import load_dotenv
from Models.DalleOpenAi import DalleOpenAi
from Models.Gpt import Gpt
from Models.StableDiffusion import StableDiffusion

load_dotenv()

DEBUG = os.getenv("DEBUG")














quantity = 2 # Cantidad de imágenes a crear: 1-10
size = "1024x1024" # Tamaño de las imágenes: 256x256, 512x512, or 1024x1024


test_prompt = "The Enchanted Forest, Capturing the enchanted essence of Nature in a lush forest setting illuminated by delicate sun rays and dotted with vibrant flower bloomsA tranquil escape from the humdrum of daily life., Nature, photography, forest, sun rays, flower blooms, tranquil, escape, enchanted, capturing, delicate"


stable_diffusion = StableDiffusion(debug=DEBUG)
stable_diffusion.generate_images(prompt=test_prompt, quantity=quantity, size=size, path='prompt-test')

exit(1)

## Instancia para comunicarse con la API de GPT
gpt = Gpt()

## Pide a la API un nuevo prompt
promptDict = gpt.next_prompt()


if not isinstance(promptDict, dict) or not promptDict['prompt']:
    print("Error al obtener el prompt")

    exit(1)

prompt = promptDict['prompt']
title = promptDict['title']
description = promptDict['description']
metatags = promptDict['metatags']





## Ver todos los modelos disponibles
#gpt.list_all_models()

## Añadir tu propio fine Tune en base a un modelo
#gpt.add_tune('photographer.jsonl')

## Instancia del modelo para Dall-e
#apiModel = DalleOpenAi(model="davinci", debug=DEBUG)

## Genera una imagen desde la api de Dall-e
#apiModel.generate_images(prompt, quantity, size)
