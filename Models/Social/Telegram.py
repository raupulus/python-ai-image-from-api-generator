#! /usr/bin/env python

import telegram
import schedule
import os
from dotenv import load_dotenv
from functions import image_resize
import tempfile
import shutil
import asyncio

load_dotenv()

class Telegram:
    def __init__(self):
        self.DEBUG = os.getenv("DEBUG")
        self.BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        self.CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
        self.BOT = telegram.Bot(token=self.BOT_TOKEN)

    async def publish(self, jsonInfo, path, max_images = 5, link = None):

        link = link or "https://aidyslexic.raupulus.dev"
        title_added = "\nSee More Seeds: " + link + "\n\n#StableDiffusion #ai #ArtificialIntelligence"
        hashtags = ' '.join(['#' + tag.replace(' ', '-') for tag in jsonInfo['tags']])

        title = jsonInfo['title'][:300]
        description = jsonInfo['description'][:500]

        text = title + "\n\n" + description + "\n\b" + title_added + "\n" + hashtags

        max_images = min(max_images, 10)

        images = []

        # Creo un directorio temporal (Para usar imágenes redimensionadas, las originales a veces se pasan de tamaño)
        temp_dir = tempfile.mkdtemp()

        ## Busco las imágenes en el path indicado y las redimensiono a máximo 1920 de ancho o alto
        for filename in os.listdir(path):
            if len(images) == max_images:
                break

            if filename.endswith(".png"):
                new_image = image_resize(image_path=path + "/" + filename, output_path=temp_dir)
                images.append(new_image)

        if (len(images) > 1):
            try:
                # Envía las imágenes junto con el texto al canal
                await self.BOT.send_media_group(chat_id=self.CHANNEL_ID, media=[telegram.InputMediaPhoto(open(image, 'rb')) for image in images], caption=text)

                #bot.send_photo(chat_id=self.CHANNEL_ID, photo=open(imagen_path, 'rb'))

                print(f'Imagenes {images} cargada con éxito.')
            except Exception as e:
                print(f'Error al cargar las imagenes {images}: {str(e)}')

        # Borro el directorio temporal y su contenido
        shutil.rmtree(temp_dir)
