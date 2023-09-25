#! /usr/bin/env python

import random
class RoleSelector:
    def __init__(self):

        self.roles_tuning = {
            "photographer": {
                "scenes": [
                    "street", "city", "nature", "landscape", "watercolor", "nature", "street", "mountain", "beach",  "forest", "sunset", "architecture", "wildlife", "portrait", "macro", "night", "urban", "cloudscape", "seascape", "countryside", "industrial", "vintage", "abstract", "underwater", "aerial", "desert", "park", "winter", "spring", "summer", "fall", "autumn", "rainforest", "lake", "river", "ocean", "cave", "alley", "fireworks", "star", "snow", "reflection", "bridge", "farm", "jungle", "village"
                ],
                "authors": [
                    "Annie Leibovitz", "Steve McCurry", "Sebastião Salgado", "Ansel Adams", "Dorothea Lange", "Joel Meyerowitz", "Henri Cartier-Bresson", "Don McCullin", "Nan Goldin", "Cindy Sherman", "Richard Avedon", "Yousuf Karsh", "Robert Capa", "Mario Testino", "Vivian Maier", "Diane Arbus", "Irving Penn", "Gordon Parks", "Edward Weston", "Man Ray", "Elliott Erwitt", "Helmut Newton", "Linda McCartney", "Mary Ellen Mark", "Eve Arnold", "Catherine Opie", "Hiroshi Sugimoto", "Duane Michals", "Alec Soth", "Nan Goldin", "Gregory Crewdson", "Nan Goldin", "Andreas Gursky", "Daido Moriyama", "Robert Frank", "Martin Parr", "Dina Goldstein", "Stephen Shore", "Bruce Davidson", "William Eggleston", "Garry Winogrand", "Nobuyoshi Araki", "Nikki S. Lee", "Joel Sternfeld", "Thomas Struth", "Lee Friedlander", "Sally Mann", "Ryan McGinley", "Nobuyoshi Araki"
                ],
                "tags": [
                    "commercial", "editorial", "fine art", "wedding", "event",
                    "fashion", "product", "architecture", "food", "travel", "sports", "documentary",
                    "black and white", "color", "HDR", "long exposure",
                    "abstract", "surreal", "conceptual", "cinematic", "panoramic", "time-lapse",
                    "high-speed", "low-key", "high-key", "bokeh", "silhouette", "monochrome", "sepia", "vignette", "depth of field",
                    "rule of thirds", "leading lines", "symmetry", "golden ratio", "perspective", "texture", "pattern", "contrast",
                    "light and shadow", "composition", "minimalism", "dramatic", "moody", "ethereal", "nostalgic", "vibrant",
                    "gritty", "dreamy", "elegant", "dynamic", "captivating", "timeless", "emotive", "evocative", "stunning",
                    "breathtaking", "iconic", "award-winning", "professional", "masterpiece", "artistic", "creative", "unique"
                ]


            }
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
        Cambia el role
        """

        self.role = list(self.roles_tuning.keys())[role]

        return role

    def get_random_tags(self):
        ## TODO: Obtener 1 escena, 1 autor y 3 tags aleatorios
        pass
