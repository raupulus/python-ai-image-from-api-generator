import openai
import os
import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

class DalleOpenAi:
    def __init__(self) -> str:
        self.image_url: str
        openai.api_key = os.getenv("API_KEY_OPENAI")
        self.APIKey = openai.api_key
        self.name = None

    def generateImage(self, prompt, model = "image-alpha-001", quantity = 1, size = "256x256"):
        try:
            self.APIKey
            response = openai.Image.create(
            prompt = prompt,
            n = quantity,
            size = size,
            )

            self.image_url = response['data']

            self.image_url = [image["url"] for image in self.image_url]

            #print(self.image_url)

            return self.image_url
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)

    def downloadImage(self, names)-> None:


        # TODO: Crear directorio si no existe
        # TODO: Paremetrizar directorio por lote, solo puede traer 10 imágenes. Si pido 50 deberían estar en el mismo directorio
        # TODO: Crear archivo de texto con metadatos (puede que venga en la url: .....org-al6rqfENpjdD0OdrrwOMlqhC/user-qLnfHYBAiEI91logB5tk84JF/img-4HRsztxQufYZFAxrElB3EpGr.png?st=2023-09-23T22%3A51%3A52Z&se=2023-09-24T00%3A51%3A52Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-23T22%3A44%3A15Z&ske=2023-09-24T22%3A44%3A15Z&sks=b&skv=2021-08-06&sig=H0evcjh1MGFKh4ZBXgcvVgHd3h1CK9rsy3XkTmNur2Y%3D)

        # TODO: Crear imágenes secuencialmente, sin espacios

        try:
            self.name = names

            for url in self.image_url:
                image = requests.get(url)

            for name in self.name:
                #with open("output/loteN/{}.png".format(name), "wb") as f:
                with open("output/{}.png".format(name), "wb") as f:
                    f.write(image.content)
        except:
            print("An error occured")

            return self.name
