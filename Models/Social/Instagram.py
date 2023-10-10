#! /usr/bin/env python

import os
import glob
from instabot import Bot
from dotenv import load_dotenv

load_dotenv()

class Instagram:
    def __init__(self):
        # Crea una instancia de Bot
        self.bot = Bot()
        self.USERNAME = os.getenv('INSTAGRAM_USERNAME')
        self.PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

    def publish(self):

        #cookie_del = glob.glob("config/*cookie.json")
        #os.remove(cookie_del[0])

        bot = self.bot

        # Inicia sesión en tu cuenta de Instagram
        bot.login(username=self.USERNAME, password=self.PASSWORD, ask_for_code=True)
        try:


            script_path = os.getcwd()

            # Lista de rutas de las imágenes que deseas publicar
            imagenes = [script_path + '/output/instagram/0.png', script_path + '/output/instagram/1.png', script_path + '/output/instagram/2.png']

            # Subir las imágenes como álbum
            media_ids = []

            for imagen in imagenes:
                media_id = bot.upload_photo(imagen)
                media_ids.append(media_id)

            # Publicar el álbum
            bot.album_upload(media_ids, caption='Spellbound Dreams in the Enchanted Village')
        except Exception as e:
            print(f'Error al publicar el tweet con imágenes: {str(e)}')
        finally:
            # Cierra sesión
            #bot.logout()
            pass


"""
from instapy_cli import clientusername = 'user' #your usernamepassword = '**********' #your password image = 'Hi_instagram.png' #here you can put the image directorytext = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'with client(username, password) as cli:    cli.upload(image, text)
"""
