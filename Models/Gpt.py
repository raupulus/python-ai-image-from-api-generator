#! /usr/bin/env python3

import os
import openai
import requests
from dotenv import load_dotenv
from time import sleep
from Models.RoleSelector import RoleSelector


load_dotenv()

class Gpt:
    current_prompt = ""

    def __init__(self, model = "gpt-3.5-turbo"):
        # Definimos el role para el GPT-3

        self.DEBUG = os.getenv("DEBUG");

        self.current_prompt = "an elephant bathing"

        openai.api_key = os.getenv("API_KEY_OPENAI")
        openai.organization = os.getenv("ORGANIZATION_OPENAI")
        openai.organization = "org-al6rqfENpjdD0OdrrwOMlqhC"

        self.APIKey = openai.api_key
        self.organization = openai.organization

        self.model = model

        self.role = RoleSelector()

    def add_tune(self, name):
        create_tune = openai.File.create(
            file=open("tuning/" + name, "rb"),
            purpose='fine-tune',
        )

        tune_id = create_tune['id']

        if self.DEBUG:
            print("Identificador de archivo subido ->tune_id: ", tune_id)

        while True:
            if self.DEBUG:
                print("Esperando que el archivo se procese...")

            file_handle = openai.File.retrieve(id=tune_id)

            if len(file_handle) and file_handle.status == "processed":
                if self.DEBUG:
                    print("File processed")

                break
            else:
                if self.DEBUG:
                    print("File not processed yet, status: ", file_handle.status)

            sleep(8)

        if self.DEBUG:
            print("file_handle: ", file_handle)

        job_created = openai.FineTuningJob.create(training_file=tune_id, model=self.model, organization_id=self.organization)

        if self.DEBUG:
            print("Job Creado: ", job_created)

        job_id = jobCreated['id']

        sleep(5)

        job_recived = openai.FineTuningJob.retrieve(id=job_id)

        if self.DEBUG:
            print("job_id: ", job_id)
            print("Job Recivido: ", job_recived)

        while job_recived and job_recived.status == 'validating_files' and not job_recived.finished_at:
            sleep(10)
            job_recived = openai.FineTuningJob.retrieve(id=job_id)
            if self.DEBUG:
                print("job_id: ", job_id)
                print("Estado del Job: ", job_recived.status)

        if self.DEBUG:
            print("Job Recivido: ", job_recived)

        organization_id = job_recived['organization_id']

        if self.DEBUG:
            print("organization_id: ", organization_id)

        # Vuelco lo que ha sucedido a un archivo de log
        log_file = open("historical.log", "a")
        log_file.write("\n*Nuevo Tune subido a la API*\n")
        log_file.write("ID del Tune subido: " + str(tune_id) + "\n")
        log_file.write("ID del Job Realizado: " + str(job_id) + "\n")
        log_file.write("ID de la organización: " + str(organization_id) + "\n")
        log_file.close()

    def remove_all_jobs(self):
        """
        Busca todos los trabajos en la api y los cancela.

        TOFIX: No funciona correctamente, necesito terminar de detectar trabajos no terminado por otro campo distinto a finished_at
        """

        jobs = openai.FineTuningJob.list(limit=100)

        for job in jobs['data']:
            job_id = job['id']

            if not job['finished_at']:
                r = openai.FineTuningJob.cancel(job_id)

        if self.DEBUG:
            print("jobs: ", jobs)

    def generate_request(self):
        model = "ft:gpt-3.5-turbo-0613:personal::82NhLBZa"

        prompt = [
            "Put yourself in the role of a professional photographer. Generate me a json that contains the fields: title, description,  metatags. It should be focused on describing a photographic scene. The title should be a few words (between 5 and 20 words) and oncise. The description should be moderately detailed and contain between 100 and 400 characters in plain text. The metatags will be a comma-separated list with a maximum of 10 words containing the most relevant information for the content described. The response cannot contain anything other than a json object. The json content must be in English. Example response: {\ntitle: \"An elephant bathing in a lake\",\ndescription: \"8k photograph of an elephant in a lake pouring water from its trunk over its head. Lake with crystal clear water and ripples due to the wind. In the background there are a few very large, green palm trees surrounding the lake. The sun is setting. There are few clouds in the sky. In the distance you can see other elephants in and out of the lake. An elephant is drinking water. There are parrots and other vibrantly colored birds near the lake and in the palm trees.\",\nmetatags: \"elephant, lake, sun, animal, photograph\"\n}",

            "Other example: {title: \"An elephant bathing in a lake\",description: \"8k photograph of an elephant in a lake pouring water from its trunk over its head. Lake with crystal clear water and ripples due to the wind. In the background there are a few very large, green palm trees surrounding the lake. The sun is setting. There are few clouds in the sky. In the distance you can see other elephants in and out of the lake. An elephant is drinking water. There are parrots and other vibrantly colored birds near the lake and in the palm trees.\",metatags: \"elephant, lake, sun, animal, photograph\"}",

            "And Other example: {\"title\": \"Golden Sunset Over Beach\",\"description\": \"A breathtaking view of the sun setting over the tranquil beaches. The sky is painted with hues of orange, pink, and purple, casting a warm and inviting glow over the sand and the calm waves of the Atlantic Ocean. People stroll along the shoreline, enjoying the serene beauty of this coastal town. The iconic lighthouse of city stands tall, silhouetted against the stunning backdrop of the setting sun, adding a touch of nostalgia to this picturesque scene.\",\"metatags\": \"sunset, beach, lighthouse, coastal, ocean\"}",

            "give me another json that contains a random suggestion in the format of the previous examples but is not similar information"
        ]

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Modelo "gpt-3.5-turbo", "gpt-3.5-turbo-instruct"...
            prompt=prompt,
            max_tokens=2000,  # Número máximo de tokens en la respuesta
            temperature=1.4,  # Temperatura de la respuesta. De 0-2, a partir de 0.8 es más random.
            #n=1,
        )


        response_message = response["choices"][0]["text"]

        if self.DEBUG:
            print("Response from API: ", response)

        return response_message


    def delete_all_tune(self):
        """
        Consulta todos los modelos generados por mi para tune de chat y los elimina.
        """

        models = openai.Model.list()

        print("models: ", models)

        # TODO: Recorrer todos los modelos y eliminarlos

    def get_prompt(self):
        """
        Devuelve el prompt actual
        :return: El prompt actual. Ej: "an elephant bathing, professional photography, high definition"
        """

        return self.current_prompt

    def next_prompt(self):
        """
        Solicita un nuevo prompt y lo devuelve
        :return: Nuevo prompt generado
        """

        new_prompt = self.generate_request()

        self.current_prompt = new_prompt

        return new_prompt

    def list_all_models(self):
        """
        Lista todos los modelos generados por mi
        """

        models = openai.Model.list(organization="org-al6rqfENpjdD0OdrrwOMlqhC",)

        print("models: ", models)
