#! /usr/bin/env python
import json
import requests
import io
import os
import base64
from PIL import Image
from dotenv import load_dotenv
import openai

load_dotenv()

class StableDiffusion:
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

    def __init__(self, model = "stable_diffusion2.15", debug = False):
        """
        model (str): Modelo de generación de imágenes.
        debug (bool): Indica si se debe imprimir información de depuración.
        """

        self.model = model
        self.DEBUG = debug

        self.url = os.getenv("STABLE_DIFFUSION_URL")

    def generate_request(self, prompt, size = "128x128", steps = 20):
        """
        Prepara y realiza la petición a la API de Stable Diffusion para generar imágenes.
        Args:
            prompt (str): Pregunta para generar imágenes.
            quantity (int): Cantidad de imágenes a generar.
            size (str): Tamaño de las imágenes a generar.
            path (str): Ruta hacia el directorio donde se guardarán las imágenes.
            steps (int): Cantidad de pasos de la generación de imágenes.
        Returns:
            None.
        Raises:
            requests.exceptions.RequestException: Ocurre cuando ocurre un error en la petición a la API de Stable Diffusion.
            Exception: Ocurre cuando ocurre un error en la petición a la API de Stable Diffusion.
        """
        url = self.url

        width = size.split("x")[0]
        height = size.split("x")[1]

        payload = {
            "prompt": prompt,
            "steps": steps,
            "seed": -1,
            "width": width,
            "height": height,
            "send_images": True,
            "sampler_index": "DPM++ 2M Karras",
        }

        try:
            response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

            if self.DEBUG:
                print("")
                print("Respuesta de la request:")
                print("http_status: ", response.status_code)
                print("Contenido: ", response.text)

            self.download_image(response.json())
        except Exception as e:
            print(e)

    def generate_images(self, prompt, quantity = 1, size = "256x256", path = None, steps = 20):
        """
        Prepara y realiza la petición a la API de Stable Diffusion para generar imágenes.
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
            name = os.urandom(2).hex() + "-" +path

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

        while pending_quantity >= 1:
            pending_quantity -= 1

            self.generate_request(prompt, size = size)

        self.is_busy = False

        return full_path

    def download_image(self, json)-> None:
        """
        Descarga una imágen a partir de un json.

        Args:
            json: Datos con la imágen en json, codificados en base64
        """

        full_path = self.current_full_path
        name = self.current_groupname
        image_name = str(self.current_pos) + ".png"

        try:

            image = Image.open(io.BytesIO(base64.b64decode(json['images'][0])))
            image.save(full_path + "/" + image_name)

            self.current_pos += 1

            if self.DEBUG:
                print("")
                print("Downloading image: " + image_name)
                print("Total: " + str(self.current_total))
                print("Pos: " + str(self.current_pos))
                print("Group: " + name)
                print("Path: " + full_path)

        except Exception as e:
            print("An error occured")
            print(e)
