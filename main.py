#! /usr/bin/env python
import os
import sys
import json
import openai
from dotenv import load_dotenv
from Models.DalleOpenAi import DalleOpenAi

load_dotenv()

DEBUG = os.getenv("DEBUG")

openai.api_key = os.getenv("API_KEY_OPENAI")

prompt = "an elephant bathing, professional photography, high definition"
quantity = 1 # Cantidad de imágenes a crear: 1-10
size = "1024x1024" # Tamaño de las imágenes: 256x256, 512x512, or 1024x1024
model = "davinci" # image-alpha-001, image-text-001


apiModel = DalleOpenAi(model=model, debug=DEBUG)

apiModel.generate_images(prompt, quantity, size)
