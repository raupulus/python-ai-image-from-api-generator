#! /usr/bin/env python

import tweepy
import os
from dotenv import load_dotenv
from functions import image_resize
import tempfile
import shutil

load_dotenv()

class Twitter:
    def __init__(self):
        self.DEBUG = os.getenv("DEBUG")
        self.consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        self.consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    def get_twitter_conn_v1(self) -> tweepy.API:
        """Get twitter conn 1.1"""

        auth = tweepy.OAuth1UserHandler(self.consumer_key, self.consumer_secret)

        auth.set_access_token(
            self.access_token,
            self.access_token_secret,
        )

        return tweepy.API(auth)

    def get_twitter_conn_v2(self) -> tweepy.Client:
        """Get twitter conn 2.0"""

        client = tweepy.Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret,
        )

        return client

    def post_tweet(self, jsonInfo, path, max_images = 4, link = None):

        link = link or "https://aidyslexic.raupulus.dev"
        title_added = "\nSee More Seeds: " + link + "\n\n#StableDiffusion #ai #ArtificialIntelligence"

        title = jsonInfo['title'][:276 - len(title_added)] + title_added  # Max 280!!!

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
                #images.append(path + "/" + filename)
                images.append(new_image)

        if (len(images) > 1):
            # Inicializo lista para almacenar los IDs de medios
            media_ids = []

            # Configuro credenciales de Twitter para ambas versiones de la API
            client_v1 = self.get_twitter_conn_v1()
            client_v2 = self.get_twitter_conn_v2()

            # Cargo las imágenes y obtiengo sus IDs de medios
            for image in images:
                try:
                    # Cargo la imagen y almaceno su ID
                    media = client_v1.media_upload(filename=image)
                    media_ids.append(media.media_id)

                    #print(f'Imagen {image} cargada con éxito.')
                except Exception as e:
                    print(f'Error al cargar la imagen {image}: {str(e)}')

            try:
                # Publica un tweet con las imágenes cargadas
                client_v2.create_tweet(text=title, media_ids=media_ids)

                if self.DEBUG:
                    #print(f'Imagenes {images} cargada con éxito.')
                    print(f'Se han publicado {len(images)} imágenes con éxito en Twitter.')
            except Exception as e:
                print(f'Error al publicar el tweet con imágenes: {str(e)}')

        # Borro el directorio temporal y su contenido
        shutil.rmtree(temp_dir)
