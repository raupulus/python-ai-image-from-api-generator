#! /usr/bin/env python

from mastodon import Mastodon as MastodonBOT
import schedule
import os
from dotenv import load_dotenv
from functions import image_resize
import tempfile
import shutil
import asyncio

load_dotenv()

class Mastodon:
    def __init__(self):
        self.DEBUG = os.getenv("DEBUG")
        self.API_URL = os.getenv("MASTODON_API_URL")
        self.CLIENT_KEY = os.getenv("MASTODON_CLIENT_KEY")
        self.CLIENT_SECRET = os.getenv("MASTODON_CLIENT_SECRET")
        self.ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")

        self.BOT = MastodonBOT(
            client_id=self.CLIENT_KEY,
            client_secret=self.CLIENT_SECRET,
            access_token=self.ACCESS_TOKEN,
            api_base_url=self.API_URL,
        )




    async def publish(self, jsonInfo, path, max_images = 4, link = None):

        link = link or "https://aidyslexic.raupulus.dev"
        hashtags = ' '.join(['#' + tag.replace(' ', '-') for tag in jsonInfo['tags']])

        title_added = "\nSee More Seeds: " + link + "\n\n#StableDiffusion #ai #ArtificialIntelligence " + hashtags
        title = jsonInfo['title'][:(500 - len(title_added))]

        current_len = len(title) + len(title_added)

        if current_len <= 300:
            slice_size = 489 - current_len
            description = jsonInfo['description'][:slice_size]

            if len(jsonInfo['description']) > slice_size:
                description += "..."

            description += "\n\b"
        else:
            description = ''

        text = title + "\n\n" + description + title_added

        if self.DEBUG:
            print(f'Longitud del texto:{len(text)}')

        max_images = min(max_images, 4)

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
            media_ids = []

            try:
                # Envía las imágenes junto con el texto al canal
                for image in images:
                    media = self.BOT.media_post(image)
                    media_ids.append(media['id'])

                if len(media_ids) > 0:
                    self.BOT.status_post(text, media_ids=media_ids)

                if self.DEBUG:
                    #print(f'Imagenes {images} cargada con éxito.')
                    print(f'Se han publicado {len(images)} imágenes con éxito en Mastodon.')
            except Exception as e:
                print(f'Error al cargar las imagenes en Mastodon {images}: {str(e)}')

        # Borro el directorio temporal y su contenido
        shutil.rmtree(temp_dir)
