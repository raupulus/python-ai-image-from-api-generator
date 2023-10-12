#! /usr/bin/env python
import json
import requests
import io
import os
import base64
from PIL import Image
from dotenv import load_dotenv
import openai
import random
from time import sleep

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

    # Array con las semillas generadas
    seeds = []

    # Indica si está ocupada la instancia trabajando con la api
    is_busy = False

    def __init__(self, role, debug = False):
        """
        model (str): Modelo de generación de imágenes.
        debug (bool): Indica si se debe imprimir información de depuración.
        """

        self.DEBUG = debug
        self.role = role

        self.url = os.getenv("STABLE_DIFFUSION_URL")

        ## Parámetros para configurar la petición api
        self.params = self.role.get_params()

    def get_seeds(self):
        """
        Devuelve las semillas generadas.
        Returns:
            list: Las semillas generadas.
        """
        return self.seeds

    def get_params(self):
        """
        Devuelve los parámetros para la petición api.
        Returns:
            dict: Los parámetros para la petición api.
        """
        return self.params

    def generate_request(self, prompt, size = "960x540"):
        """
        Prepara y realiza la petición a la API de Stable Diffusion para generar imágenes.
        Args:
            prompt (str): Pregunta para generar imágenes.
            quantity (int): Cantidad de imágenes a generar.
            size (str): Tamaño de las imágenes a generar.
            path (str): Ruta hacia el directorio donde se guardarán las imágenes.
        Returns:
            None.
        Raises:
            requests.exceptions.RequestException: Ocurre cuando ocurre un error en la petición a la API de Stable Diffusion.
            Exception: Ocurre cuando ocurre un error en la petición a la API de Stable Diffusion.
        """
        url = self.url

        width = size.split("x")[0]
        height = size.split("x")[1]

        current_seed = random.randint(0, 2**32 - 1)

        render = self.role.get_render()

        if render:
            prompt += f" {render}"

        payload = {
            "prompt": prompt,
            "negative_prompt": self.params.get("negative_prompt"),
            #"styles": [""],
            "model": self.params.get("model"), # 'sd_v2.1_768_v_f16.ckpt', 'realistic_vision_v3.0_q6p_q8p.ckpt',
            "steps": int(self.params.get("steps")),
            "cfg_scale": float(self.params.get("cfg_scale")),
            "seed": current_seed,
            "width": int(width),
            "height": int(height),
            "sampler_index": self.params.get("sampler_index"), # "DPM++ 2M Karras"
            "restore_faces": bool(self.params.get("restore_faces")),
            "batch_size": 1,
            "n_iter": 1,
            "denoising_strength": float(self.params.get("denoising_strength")),
            "refiner_model": "sd_xl_refiner_1.0_f16.ckpt",
            #"seed": 479748350
            #"seed_mode": "NVIDIA GPU Compatible"
            #"save_images": False,
            #"send_images": True,
            #"hr_scale": 4,
            #"hr_upscaler": "R-ESRGAN 4x+",
            #"hr_second_pass_steps": 0,
            #"hr_resize_x": 0,
            #"hr_resize_y": 0,
            #"hr_checkpoint_name": "string",
            #"hr_sampler_name": "string",
            #"hr_prompt": "",
            #"hr_negative_prompt": "",

        }

        if self.DEBUG:
            print("")
            print("Generando imagen...")

        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

        if self.DEBUG:
            print("")
            print("Respuesta de la request:")
            print("http_status: ", response.status_code)
            print("Contenido: ", response.text)

        response_json =  response.json()

        self.download_image(response_json)

        if self.DEBUG and response_json.get('info'):
            print("")
            print("Información recibida para la imagen generada:")
            print(response_json.info)

        if self.DEBUG and response_json.get('parameters'):
            print("")
            print("Parámetros recibidos para la imagen generada:")
            print(response_json.parameters)

        ## Elimino la imagen del objeto json para mostrar el resto de datos al depurar
        if self.DEBUG:
            del response_json['images']

            print(f"Otros parámetros recibidos para la imagen generada: {response_json}")

        #current_seed = response_json.parameters['seed']
        self.seeds.append(current_seed)

    def generate_images(self, prompt, quantity = 1, size = "256x256", path = None):
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
            name = os.urandom(2).hex() + " - " +path

        self.params = self.role.get_params()
        self.seeds = []
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
        errors = 0

        while pending_quantity >= 1:
            pending_quantity -= 1

            ## Previene errores en bucle, si en 5 intentos no genera imagen hay que revisar algo.
            if errors >= 5:
                print("Ha ocurrido un error al generar la imagen y no se puede continuar")

                exit(1)

            try:
                self.generate_request(prompt, size = size)

                errors = 0
            except Exception as e:
                print("Ha ocurrido un error al generar la imagen")
                print(e)
                print("Intentando de nuevo en 3 segundos...")
                pending_quantity += 1
                errors += 1
                sleep(3)

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

        image = Image.open(io.BytesIO(base64.b64decode(json['images'][0])))
        image.save(full_path + "/" + image_name)

        self.current_pos += 1

        if self.DEBUG:
            print("")
            print("Downloading image: " + image_name)
            print(f"Generadas: {str(self.current_pos)} de {str(self.current_total)}")
            print("Group: " + name)
            print("Path: " + full_path)
