#! /usr/bin/env python3
import requests
from dotenv import load_dotenv
import os
import re
import json
import base64
from time import sleep
from PIL import Image

load_dotenv()

class Api:
    headers = {
        'Authorization': 'Bearer ' + os.getenv("API_KEY"),
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def __init__(self):
        self.debug = os.getenv("DEBUG")
        self.api_key = os.getenv("API_KEY")
        self.url_create = os.getenv("API_URL_CREATE")
        self.url_update = os.getenv("API_URL_UPDATE")


    def createCollection(self, jsonInfo):
        """
        Envía datos de la colección a la API para crearla.

        Args:
            jsonInfo (dict): Diccionario con los datos de la colección
        """

        response = requests.post(url=self.url_create, json=jsonInfo, headers=self.headers)

        if response.status_code != 200:
            print("API Error al crear la colección")
            print("API http_status: ", response.status_code)
            print("API Contenido: ", response.text)

            return

        response_json = response.json()

        return response_json['data']['collection_id']

    def addImageToCollection(self, collection_id, order, image_path):

        with open(image_path, "rb") as f:
            im_bytes = f.read()

        image = base64.b64encode(im_bytes).decode("utf8")

        url = f"{self.url_update}/{collection_id}"

        json = {
            "order": order,
            "image": image,
        }

        response = requests.post(url=url, json=json, headers=self.headers)

        if response.status_code != 200:
            print("API Error al subir imagen en la colección")
            print("API http_status: ", response.status_code)
            print("API Contenido: ", response.text)

            return False

        response_json = response.json()

        return response_json.get('success') or False

    def directoryUpload(self, jsonInfo, path):
        """
        Procesa la subida de una nueva colección con todas las imágenes.
        Args:
            jsonInfo (dict): Información de la colección e imágenes.
            path (str): Directorio de la colección, ruta absoluta.
        """

        collection_id = self.createCollection(jsonInfo)

        max_retries = 5
        errors = 0

        elments_in_path = os.listdir(path);
        images_list = []

        for filename in elments_in_path:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images_list.append(filename)

        images_list.sort(key=lambda s: int(re.search(r'\d+', s).group()))

        # Recorro todo el directorio de imágenes para subirlas a la colección
        for idx, filename in enumerate(images_list):
            print(f"Subiendo imagen {idx} de la colección {collection_id}")
            print(f"Imagen: {filename}")

            while not self.addImageToCollection(collection_id, idx, path + "/" + filename):
                errors += 1
                sleep(5)

                # Si hay más de 3 errores, salimos del bucle
                if errors >= max_retries:
                    print(f"Ha ocurrido más de {max_retries} errores, saliendo de la subida de la colección")
                    errors = 0

                    break

            errors = 0
            sleep(0.3)
