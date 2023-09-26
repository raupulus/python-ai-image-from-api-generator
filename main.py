#! /usr/bin/env python
import os
from dotenv import load_dotenv
from Models.DalleOpenAi import DalleOpenAi
from Models.Gpt import Gpt

load_dotenv()

DEBUG = os.getenv("DEBUG")

quantity = 2 # Cantidad de imágenes a crear: 1-10
size = "1024x1024" # Tamaño de las imágenes: 256x256, 512x512, or 1024x1024

## Instancia para comunicarse con la API de GPT
gpt = Gpt()

## Pide a la API un nuevo prompt
prompt = gpt.next_prompt()

## Ver todos los modelos disponibles
#gpt.list_all_models()

## Añadir tu propio fine Tune en base a un modelo
#gpt.add_tune('photographer.jsonl')

## Instancia del modelo para Dall-e
#apiModel = DalleOpenAi(model="davinci", debug=DEBUG)

## Genera una imagen desde la api de Dall-e
#apiModel.generate_images(prompt, quantity, size)
