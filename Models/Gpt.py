#! /usr/bin/env python3

import os
import openai
import requests
from dotenv import load_dotenv
from time import sleep
import json
import re

load_dotenv()

class Gpt:
    ## Cadena de texto con el último prompt generado.
    current_prompt = None

    ## Diccionario con los datos para generar el prompt actual {title: "", "descrption": "", "metatags": ""}
    current_prompt_data = None


    def __init__(self, role, model = "gpt-3.5-turbo-instruct"):
        """
        Args:
            model (str): Modelo de generación de texto.
        """

        # Definimos el role para el GPT-3

        self.DEBUG = os.getenv("DEBUG");

        self.current_prompt = "an elephant bathing"

        openai.api_key = os.getenv("API_KEY_OPENAI")
        openai.organization = os.getenv("ORGANIZATION_OPENAI")

        self.APIKey = openai.api_key
        self.organization = openai.organization

        self.model = model

        self.role = role

    def add_tune(self, name):
        """
        Agrega un tune a la API de OpenAI. Esto es principalmente para modelos de chat.

        Args:
            name (str): Nombre del archivo a subir.
        """
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
        """
        Genera un nuevo prompt en base a un role aleatorio y lo devuelve.

        :return: Nuevo prompt generado
        """
        model = self.model
        role = self.role

        ## Obtengo los prompts en base al role elegido
        prompts = role.get_prompts()

        response = openai.Completion.create(
            engine=self.model,  # Modelo "gpt-3.5-turbo", "gpt-3.5-turbo-instruct"...
            prompt=prompts,
            max_tokens=2000,  # Número máximo de tokens en la respuesta
            temperature=1.4,  # Temperatura de la respuesta. De 0-2, a partir de 0.8 es más random.
            user='python-ai-image-from-api-generator',
            n=1,
        )

        response_message = response["choices"][0]["text"]
        response_message = re.sub('\W+\s\{\}','', response_message)

        if self.DEBUG:
            print("Response from API: ", response)

        compiled = re.compile(re.escape("title"), re.IGNORECASE)
        response_message = compiled.sub("title", response_message)

        compiled = re.compile(re.escape("description"), re.IGNORECASE)
        response_message = compiled.sub("description", response_message)

        compiled = re.compile(re.escape("metatags"), re.IGNORECASE)
        response_message = compiled.sub("metatags", response_message)

        compiled = re.compile(r"\s+")
        response_message = compiled.sub(" ", response_message).strip()

        start_of_json = response_message.find("{")
        end_of_json = response_message.find("}")

        response_message = response_message[start_of_json:(end_of_json + 1)]

        return response_message.strip() \
            .replace(r"\n", "") \
            .replace(r"\t", "") \
            .replace(r"\r", "") \
            .replace(r"\`", "") \
            .replace(r"\.", '') \
            .replace(r'.', '') \
            .replace(r"\>", "") \
            .replace(r"\/", "") \
            .replace(r"\s*", ' ') \
            .replace(r"\“", "\"") \
            .replace(r"\”", "\"") \
            .replace(r"\*", "") \
            .replace(r"\_", "")


    def next_prompt(self):
        """
        Solicita un nuevo prompt y lo devuelve

        :return: Nuevo prompt generado
        """

        ## Establezco un role aleatorio para componer el prompt
        self.role.set_random_role()

        counter = 1 # Contador de intentos para obtener json
        limit = 5 # Máximo de intentos para obtener json
        new_prompt = None
        new_prompt_data = None

        while counter <= limit and (new_prompt is None or new_prompt_data is None):
            counter += 1

            new_prompt = self.generate_request()

            if self.DEBUG:
                print("")
                print("new_prompt antes de decodificar JSON: ", new_prompt)
                print("")

            if new_prompt and len(new_prompt):
                try:
                    new_prompt_data = json.loads(new_prompt)

                    metatags = new_prompt_data["metatags"]

                    if isinstance(metatags, list) and len(metatags) > 0:
                        metatags = ",".join(metatags)

                    title = re.sub('\W+\s\:','', new_prompt_data["title"]).replace(r':', '').replace(r'-', ' ')
                    description = re.sub('\W+\s\-','', new_prompt_data["description"]).replace(r':', ' ')

                    new_prompt = title + ", " + description + ", " + metatags

                except Exception as e:
                    if self.DEBUG:
                        print("An error occured")
                        print(e)
                        print("ERROR PROMPT: ", new_prompt)

                    new_prompt = None
                    new_prompt_data = None

        self.current_prompt = new_prompt
        self.current_prompt_data = new_prompt_data

        if self.DEBUG:
            print("new_prompt: ", new_prompt)
            print("")
            print("new_prompt_data: ", new_prompt_data)

        return {
            "prompt": new_prompt,
            "title": title,
            "description": description,
            "metatags": metatags,
        }

    def delete_all_tune(self):
        """
        Consulta todos los modelos generados por mi para tune de chat y los elimina.

        TODO: Recorrer todos los modelos y eliminarlos
        """

        models = openai.Model.list()

        if self.DEBUG:
            print("models: ", models)

    def get_prompt(self):
        """
        Devuelve el prompt actual

        :return: El prompt actual. Ej: "an elephant bathing, professional photography, high definition"
        """

        return self.current_prompt

    def get_prompt_data(self):
        """
        Devuelve el diccionario con la información para generar el prompt actual
        """

        return self.current_prompt_data

    def list_all_models(self):
        """
        Lista todos los modelos generados por mi
        """

        models = openai.Model.list(organization=self.organization)

        print("")
        print("models: ", models)
        print("")

    def generate_prompts_to_csv(self, quantity):
        """
        Genera un listado de prompts y los almacena en el directorio de salida
        dentro de un archivo CSV.

        Args:
            quantity (int): Cantidad de prompts a generar.
        """

        counter = 0

        script_path = os.getcwd()
        full_path = script_path + "/output/batch_prompts.csv"

        if not os.path.exists(full_path):
            with open(full_path, "w") as file:
                file.write("title;description;metatags;prompt\n")

            file.close()

        while counter < quantity:
            counter += 1

            ## Obtengo un nuevo prompt
            promptDict = self.next_prompt()

            ## Extraigo los datos del nuevo prompt
            prompt = promptDict['prompt'].strip()
            title = promptDict['title'].strip()
            description = promptDict['description'].strip()
            metatags = promptDict['metatags'].strip()

            if not prompt:
                counter -= 1

                sleep(5)

                continue

            with open(full_path, "a") as file:
                file.write(title + ";" + description + ";" + metatags + ";" + prompt + "\n")

            file.close()
