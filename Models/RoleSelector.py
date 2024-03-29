#! /usr/bin/env python

import random
import json
import os
from dotenv import load_dotenv
import Data.photographer as data_photographer
import Data.photographer_people as data_photographer_people
import Data.photographer_animals as data_photographer_animals
import Data.photographer_food as data_photographer_food
import Data.artist as data_artist
import Data.artist_monster as data_artist_monster
import Data.art_2d_people as data_art_2d_people
import Data.art_3d_people as data_art_3d_people
import Data.art_fantasy as data_art_fantasy

load_dotenv()

class RoleSelector:

    def __init__(self):
        self.DEBUG = os.getenv("DEBUG")

        self.roles_tuning = {
            "photographer": data_photographer.getData(),
            "photographer_people": data_photographer_people.getData(),
            "photographer_animals": data_photographer_animals.getData(),
            "photographer_food": data_photographer_food.getData(),
            "artist": data_artist.getData(),
            "artist_monster": data_artist_monster.getData(),
            "art_2d_people": data_art_2d_people.getData(),
            "art_3d_people": data_art_3d_people.getData(),
            "art_fantasy": data_art_fantasy.getData(),
        }

        # Establezco un role aleatorio al instanciarse
        self.set_random_role()

    def set_random_role(self):
        """
        Establece un role aleatorio
        """

        # Obtengo la cantidad de roles disponibles
        quantity = len(self.roles_tuning)

        # Obtengo un indice aleatorio entre 0 y la cantidad de roles disponibles - 1
        role_index = random.randint(0, quantity - 1)

        # Obtengo el role de ese indice
        role = list(self.roles_tuning.keys())[role_index]

        self.role = role

        return role

    def change_role(self, role):
        """
        Cambia el role a uno existente concreto.

        Args:
            role (str): El role a cambiar.

        Returns:
            str: El role actual.
        """

        self.role = role

        return self.role

    def get_render(self):
        """
        Devuelve el render del role actual.

        Returns:
            str|None: El render del role actual.
        """

        return self.roles_tuning[self.role].get("render", None)

    def get_prompts(self):
        """
        Devuelve todos los prompts para el role actual.

        Returns:
            list: Los prompts para el role actual.
        """

        file = 'tuning' + "/" + self.roles_tuning[self.role]["file"] + ".jsonl"

        role_description = self.roles_tuning[self.role]["description"]

        # Escena, autor y etiqueta
        scene = random.choice(self.roles_tuning[self.role]["scenes"])
        author = random.choice(self.roles_tuning[self.role]["authors"])
        tags = random.choice(self.roles_tuning[self.role]["tags"])
        element = random.choice(self.roles_tuning[self.role]["elements"])

        first_prompt = f"{role_description} inspired by author \"{author}\" . Generate me a json that contains the fields: title, description, metatags. You should focus on describing this scene: {scene}. In the described scene, this element should appear: {element}. Some tags to keep in mind when describing the title and scene: {tags}. The title should be a few words (between 7 and 25 words) and oncise. The description should be moderately detailed and contain between 40 and 400 characters in plain text. The metatags will be a comma-separated list with a maximum of 10 words containing the most relevant information for the content described. The response cannot contain anything other than a json object. The json content must be in English."


        additional_text = f"The content must adapt to the following description, Type of scene: {scene}. Suggestion inspired by author: {author}. You must include these tags in the description: {tags}. Must include: {element}."

        prompts = []

        # Leer el archivo JSONL
        with open(file, "r") as file:
            prompts = [json.loads(line.strip()).get("prompt") for line in file]

        file.close()

        prompts.insert(0, first_prompt)


        prompts.append(f"Returns only json valid format as in the previous examples, no spaces, no line breaks, no extraneous characters, no text outside the string with the json. With the attributes: \"title\", \"description\" and \"metatags\". {additional_text}")

        if (self.DEBUG):
            #print("PROMPTS:")
            #print(prompts)
            print("")
            print(f"Role Actual: {self.role}")
            print(f"Scene: {scene}")
            print(f"Inspired by the author: {author}")
            print(f"Tags: {tags}")
            print(f"Element: {element}")
            print("")

        return prompts

    def get_params(self):
        """
        Devuelve los parámetros para el role actual.

        Returns:
            dict: Los parámetros para el role actual.
        """

        return self.roles_tuning[self.role]["params"]
