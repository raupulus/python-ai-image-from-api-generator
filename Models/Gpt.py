#! /usr/bin/env python3

import os
import openai
import requests
from dotenv import load_dotenv
from time import sleep

load_dotenv()

class Gpt:
    current_prompt = ""

    tunings = {
        "photographer": "file-KYEitEh4VKARTkr1Lfnc4DUR",
        "cartoonist": "file-5PZU37dqJuNALawx0MIN2Hde    ????",
        "artist"      : "file-5PZU37dqJuNALawx0MIN2Hde    ?????",
    }

    def __init__(self, model = "gpt-3.5-turbo"):
        # Definimos el role para el GPT-3
        self.current_prompt = "an elephant bathing"

        openai.api_key = os.getenv("API_KEY_OPENAI")
        #openai.organization = os.getenv("ORGANIZATION_OPENAI")
        openai.organization = "org-al6rqfENpjdD0OdrrwOMlqhC"
        self.APIKey = openai.api_key

        self.model = model

    def add_tune(self, name):
        create_tune = openai.File.create(
            file=open("tuning/" + name, "rb"),
            purpose='fine-tune',
        )

        tune_id = create_tune['id']

        print("tune_id: ", tune_id)

        while True:
            print("Esperando que el archivo se procese...")

            file_handle = openai.File.retrieve(id=tune_id)

            if len(file_handle) and file_handle.status == "processed":
                print("File processed")

                break
            else:
                print("File not processed yet, status: ", file_handle.status)

            sleep(8)

        print("file_handle: ", file_handle)

        r2 = openai.FineTuningJob.create(training_file=tune_id, model=self.model, organization_id="org-al6rqfENpjdD0OdrrwOMlqhC")

        print("r2: ", r2)

        job_id = r2['id']


        sleep(5)

        r3 = openai.FineTuningJob.retrieve(id=job_id)


        print("job_id: ", job_id)
        print("r3: ", r3)

        while r3 and r3.status == 'validating_files' and not r3.finished_at:
            sleep(10)
            r3 = openai.FineTuningJob.retrieve(id=job_id)
            print("status: ", r3.status)

        print("r3: ", r3)

        organization_id = r3['organization_id']

        print("organization_id: ", organization_id)

        # Vuelco lo que ha sucedido a un archivo de log
        log_file = open("historical.log", "a")
        log_file.write("ID del Tune subido: " + str(tune_id) + "\n")
        log_file.write("ID del Job Realizado: " + str(job_id) + "\n")
        log_file.write("ID de la organización: " + str(organization_id) + "\n")
        log_file.close()

    def remove_all_jobs(self):
        """
        Busca todos los trabajos en la api y los cancela.
        """

        jobs = openai.FineTuningJob.list(limit=100)

        #print("jobs: ", jobs)

        for job in jobs['data']:
            job_id = job['id']

            if not job['finished_at']:
                r = openai.FineTuningJob.cancel(job_id)




        print("jobs: ", jobs)

    def generate_request(self):
        #model = "ft:gpt-3.5-turbo-0613:org-al6rqfENpjdD0OdrrwOMlqhC::file-KYEitEh4VKARTkr1Lfnc4DUR"
        model = "ft:gpt-3.5-turbo-0613:personal::82NhLBZa"

        messages = [
            {
                "role": "system",
                "content": "You are a prompt generator that only responds to a suggestion for the user to create a real or fictitious image of animals or non-real beings from your text suggestion. Responses must contain labels with more details separated by commas until reaching a minimum of 200 characters and a maximum of 800 characters."
            },


        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )

        response_message = response["choices"][0]["message"]

        #print("")
        #print("response: ", response)
        #print("")
        #print("response_message: ", response_message)
        #print("")

        return response_message["content"]


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
