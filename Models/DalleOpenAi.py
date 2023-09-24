import openai
import os
import requests
from PIL import Image
from dotenv import load_dotenv
from time import sleep

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
        openai.api_key = os.getenv("API_KEY_OPENAI")
        self.APIKey = openai.api_key
        self.model = model
        self.DEBUG = debug

    def generate_request(self, prompt, quantity = 1, size = "256x256"):

        try:
            response = openai.Image.create(
                prompt = prompt,
                n = quantity,
                size = size,
                model = self.model
            )

            datas = response['data']

            urls = [data["url"] for data in datas]

            self.download_images(urls)
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)


    def generate_images(self, prompt, quantity = 1, size = "256x256", path = None):
        while self.is_busy:
            print("Esperando a que la API esté disponible...")

            sleep(5)

        if path is None:
            name = os.urandom(16).hex()
        else:
            name = path

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

    def download_images(self, urls)-> None:
        """
        Args:
            urls (dic): Urls con la ruta a las imágenes
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
