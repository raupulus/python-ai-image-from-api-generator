#! /usr/bin/env python
import os
import sys
import json
import openai
from dotenv import load_dotenv
from Models.DalleOpenAi import DalleOpenAi
from Models.Gpt import Gpt


load_dotenv()

DEBUG = os.getenv("DEBUG")

openai.api_key = os.getenv("API_KEY_OPENAI")

quantity = 2 # Cantidad de imágenes a crear: 1-10
size = "1024x1024" # Tamaño de las imágenes: 256x256, 512x512, or 1024x1024


gpt = Gpt(model="gpt-3.5-turbo")

#gpt.list_all_models()

#gpt.add_tune('photographer.jsonl')

apiModel = DalleOpenAi(model="davinci", debug=DEBUG)


prompt = gpt.next_prompt()
print("nextPromt: ", prompt)

#apiModel.generate_images(prompt, quantity, size)

exit(1)
prompt = gpt.next_prompt()
print("nextPromt: ", prompt)
apiModel.generate_images(prompt, quantity, size)


prompt = gpt.next_prompt()
print("nextPromt: ", prompt)
apiModel.generate_images(prompt, quantity, size)
