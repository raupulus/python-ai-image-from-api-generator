#! /usr/bin/env python3

import openai
import os
import requests
from PIL import Image
from time import sleep
from dotenv import load_dotenv

load_dotenv()


class DalleOpenAi:
    # Posición actual iterando imágenes del lote
    current_pos = 0

    # Total de imágenes para el lote actual
    current_total = 0

    # Nombre del lote actual de imágenes para agruparlas por directorio
    current_groupname = "lote"

    # Ruta hacia el lote de imágenes actual
    current_full_path = 'output/lote'

    # Indica si está ocupada la instancia trabajando con la api
    is_busy = False


    def __init__(self, model = "davinci", debug = False) -> str:
        """
        model (str): Modelo de generación de imágenes.
        debug (bool): Indica si se debe imprimir información de depuración.
        """

        openai.api_key = os.getenv("API_KEY_OPENAI")
        self.APIKey = openai.api_key
        self.model = model
        self.DEBUG = debug

    def generate_request(self, prompt, quantity = 1, size = "256x256"):
        """
        Prepara y realiza la petición a la API de OpenAI para generar imágenes.
        Args:
            prompt (str): Pregunta para generar imágenes.
            quantity (int): Cantidad de imágenes a generar.
            size (str): Tamaño de las imágenes a generar.
            path (str): Ruta hacia el directorio donde se guardarán las imágenes.
            model (str): Modelo de generación de imágenes.
            debug (bool): Indica si se debe imprimir información de depuración.
        Returns:
            None.
        Raises:
            openai.error.OpenAIError: Ocurre cuando ocurre un error en la petición a la API de OpenAI.
            requests.exceptions.RequestException: Ocurre cuando ocurre un error en la petición a la API de OpenAI.
            Exception: Ocurre cuando ocurre un error en la petición a la API de OpenAI.
        """
        try:
            response = openai.Image.create(
                prompt = prompt,
                n = quantity,
                size = size,
                #model = self.model
            )

            datas = response['data']

            urls = [data["url"] for data in datas]

            self.download_images(urls)
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)


    def generate_images(self, prompt, quantity = 1, size = "256x256", path = None):
        """
        Genera imágenes con la API de OpenAI.
        Args:
            prompt (str): Descripción para generar imágenes.
            quantity (int): Cantidad de imágenes a generar.
            size (str): Tamaño de las imágenes a generar.
            path (str): Nombre del directorio donde se guardarán las imágenes.
        Returns:
            Devuelve el directorio con ruta absoluta hacia la nueva galería.
        """
        while self.is_busy:
            print("Esperando a que la API esté disponible...")

            sleep(5)

        if path is None:
            name = os.urandom(16).hex()
        else:
            name = name = os.urandom(2).hex() + "-" + path

        self.current_groupname = name

        script_path = os.getcwd()
        full_path = script_path + "/output/" + name

        self.current_full_path = full_path

        if os.path.exists(script_path) and not os.path.exists(full_path):
            os.makedirs(full_path, exist_ok=True)

        self.is_busy = True

        self.current_pos = 0
        self.current_total = quantity

        pending_quantity = quantity

        while pending_quantity >= 10:
            pending_quantity -= 10
            self.generate_request(prompt, quantity = 10, size = size)

        if pending_quantity >= 1 and pending_quantity < 10:
            self.generate_request(prompt, quantity = pending_quantity, size = size)

        self.is_busy = False

        return full_path

    def download_images(self, urls)-> None:
        """
        Descarga las imágenes de la lista de URLs.
        Args:
            urls (list): Lista de URLs de imágenes.
        Returns:
            None.
        """

        full_path = self.current_full_path
        name = self.current_groupname

        try:
            for url in urls:
                image = requests.get(url)
                image_name = str(self.current_pos) + ".png"
                self.current_pos += 1

                if self.DEBUG:
                    print("")
                    print("Downloading image: " + image_name)
                    print("Total: " + str(self.current_total))
                    print("Pos: " + str(self.current_pos))
                    print("Group: " + name)
                    print("Path: " + full_path)

                with open(full_path + "/" + image_name, "wb") as f:
                    f.write(image.content)

        except Exception as e:
            print("An error occured")
            print(e)
