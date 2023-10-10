#! /usr/bin/env python

import tweepy
import os
from dotenv import load_dotenv

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

    def post_tweet(self, jsonInfo, path, max_images = 4):

        title = jsonInfo['title'][:230] + "\nMore Seeds: https://aidyslexic.raupulus.dev/" # Max 280!!!

        max_images = min(max_images, 4)

        images = []

        ## Busco las imágenes en el path indicado
        for filename in os.listdir(path):
            if len(images) == max_images:
                break

            if filename.endswith(".png"):
                images.append(path + "/" + filename)

        if (len(images) > 1):
            # Inicializa una lista para almacenar los IDs de medios
            media_ids = []

            # Configura tus credenciales de Twitter
            client_v1 = self.get_twitter_conn_v1()
            client_v2 = self.get_twitter_conn_v2()

            # Carga las imágenes y obtiene sus IDs de medios
            for image in images:
                try:
                    # Carga la imagen y almacena su ID
                    media = client_v1.media_upload(filename=image)
                    media_ids.append(media.media_id)

                    print(f'Imagen {image} cargada con éxito.')
                except Exception as e:
                    print(f'Error al cargar la imagen {image}: {str(e)}')

            # Publica un tweet con las imágenes cargadas
            try:
                # Publica el tweet con la imagen
                client_v2.create_tweet(text=title, media_ids=media_ids)

                print('Tweet con imagen publicado con éxito.')
            except Exception as e:
                print(f'Error al publicar el tweet con imágenes: {str(e)}')
