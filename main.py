#! /usr/bin/env python
import os
import sys
import json
import openai
from dotenv import load_dotenv
from Models.DalleOpenAi import DalleOpenAi

load_dotenv()

openai.api_key = os.getenv("API_KEY_OPENAI")

prompt = "an elephant bathing, professional photography, high definition"
quantity = 1 # Cantidad de imágenes a crear: 1-10
size = "1024x1024" # Tamaño de las imágenes: 256x256, 512x512, or 1024x1024
model = "davinci" # image-alpha-001, image-text-001


#DATA_DIR = Path.cwd() / "output/lote1"
#DATA_DIR.mkdir(exist_ok=True)

dalleOpenAi = DalleOpenAi()

dalleOpenAi.generateImage(prompt, model, quantity, size)

dalleOpenAi.downloadImage(names=[
"test1",
])

exit(1)

response = openai.Image.create(
    prompt=prompt,
    model=model,
    n=quantity,
    size=size,
    response_format="b64_json" # url, b64_json
)

print(response)

"""
# A partir de otra imagen
response = openai.Image.create_edit(
image=open("sunlit_lounge.png", "rb"),
mask=open("mask.png", "rb"),
prompt="A sunlit indoor lounge area with a pool containing a flamingo",
n=1,
size="1024x1024"
)
"""

#file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"


#with open(file_name, mode="w", encoding="utf-8") as file:
#    json.dump(response, file)


#print(response["data"][0]["url"])
