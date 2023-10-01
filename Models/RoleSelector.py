#! /usr/bin/env python

import random
import json
import os
from dotenv import load_dotenv

load_dotenv()

class RoleSelector:
    def __init__(self):

        self.DEBUG = os.getenv("DEBUG")

        self.roles_tuning = {
            "photographer": {
                "description": "Put yourself in the role of a professional photographer",
                "file": "photographer", ## Archivo dentro del directorio "tuning"
                "scenes": [
                    "street", "city", "nature", "landscape", "watercolor", "street", "mountain", "beach",  "forest", "sunset", "architecture", "wildlife", "portrait", "macro", "night", "urban", "cloudscape", "seascape", "countryside", "industrial", "vintage", "abstract", "underwater", "aerial", "desert", "park", "winter", "spring", "summer", "fall", "autumn", "rainforest", "lake", "river", "ocean", "cave", "alley", "fireworks", "star", "snow", "reflection", "bridge", "farm", "jungle", "village"
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
                    "breathtaking", "iconic", "award-winning", "professional", "masterpiece", "artistic", "creative", "unique",
                    "abstract", "pattern", "texture", "reflection", "silhouette",
                    "emotions", "love", "happiness", "sadness", "surprise", "fear", "anger",
                    "vintage", "retro", "modern", "minimalism"
                ],
                "elements": [
                    "people", "portrait", "model", "celebrity", "child", "adult", "elderly", "man", "woman", "couple", "group",
                    "animal", "pets", "wildlife", "bird", "mammal", "reptile", "insect", "fish",
                    "nature", "landscape", "tree", "flower", "plant", "sky", "clouds", "sun", "moon", "stars", "rainbow",
                    "architecture", "building", "house", "skyscraper", "bridge", "church", "castle", "ruins",
                    "food", "meal", "restaurant", "dish", "dessert", "drink", "coffee", "wine", "cocktail",
                    "travel", "destination", "cityscape", "street", "road", "beach", "mountain", "lake", "river", "ocean", "island", "countryside",
                    "vehicle", "car", "bike", "motorcycle", "bus", "train", "airplane", "boat", "subway", "helicopter",
                    "event", "wedding", "party", "concert", "festival", "sporting event", "conference", "parade",
                    "fashion", "clothing", "accessories", "shoes", "jewelry", "makeup", "hairstyle",
                    "technology", "computer", "smartphone", "camera", "drone", "gadget", "robot",
                    "art", "sculpture", "painting", "music", "instrument", "dance", "theater",
                    "books", "reading", "library", "study", "writing", "pen", "notebook",
                    "work", "office", "meeting", "workplace", "tools", "equipment", "construction",
                    "adventure", "exploration", "journey", "discovery", "hiking", "camping",
                    "industry", "factory", "manufacturing", "construction", "technology",
                    "health", "medical", "hospital", "doctor", "nurse", "patient",
                    "education", "school", "classroom", "learning", "student", "teacher",
                    "family", "parenting", "children", "relationship", "love", "friendship",
                    "community", "people", "diversity", "culture", "celebration", "holiday", "tradition", "festive"
                ]
            },
            "artist": {
                "description": "Put yourself in the role of a professional graphic design and painting artist",
                "file": "artist", ## Archivo dentro del directorio "tuning"
                "scenes": [
                    "street", "city", "nature", "landscape", "watercolor", "street", "mountain", "beach",  "forest", "sunset", "architecture", "wildlife", "portrait", "macro", "night", "urban", "cloudscape", "seascape", "countryside", "industrial", "vintage", "abstract", "underwater", "aerial", "desert", "park", "winter", "spring", "summer", "fall", "autumn", "rainforest", "lake", "river", "ocean", "cave", "alley", "fireworks", "star", "snow", "reflection", "bridge", "farm", "jungle", "village"
                ],
                "authors": ["Banksy", "Jeff Koons", "Damien Hirst", "Yayoi Kusama",
                    "Takashi Murakami", "Ai Weiwei", "Cindy Sherman", "Kehinde Wiley",
                    "Kara Walker", "Julie Mehretu", "Gerhard Richter", "David Hockney", "Anish Kapoor", "Tracey Emin", "Yoko Ono",
                    "Olafur Eliasson", "Marina Abramović", "Kusama Yayoi", "Hockney David", "Ai Wei Wei", "JR", "Hockney David", "Chris Ofili",
                    "Jenny Holzer", "Nan Goldin", "Kiki Smith", "Rirkrit Tiravanija", "Matthew Barney", "Louise Bourgeois", "Wolfgang Tillmans",
                    "Cai Guo-Qiang", "Barbara Kruger", "Yinka Shonibare", "Shirin Neshat", "Yan Pei-Ming", "Elizabeth Peyton",
                    "Mariko Mori", "Mona Hatoum", "Mickalene Thomas", "Luc Tuymans", "Elizabeth Peyton", "Cecily Brown", "Tom Sachs",
                    "Maurizio Cattelan", "Shirin Neshat", "Do Ho Suh", "Sterling Ruby", "Carrie Mae Weems", "William Kentridge",
                    "Marlene Dumas", "Lorna Simpson", "Kerry James Marshall", "Glenn Ligon", "Elizabeth Murray", "Sean Scully",
                    "Philip Guston", "Frida Kahlo", "Vija Celmins", "Catherine Opie", "Kara Walker", "Gilbert & George",
                    "Zhang Xiaogang", "Liu Xiaodong", "Yue Minjun", "Fang Lijun", "Zeng Fanzhi", "Zhang Huan", "Yan Pei-Ming", "Xu Bing",
                    "Xiao Lu", "Wang Guangyi", "Zao Wou-Ki", "Chen Danqing", "Yue Minjun", "Huang Yong Ping", "Liu Bolin", "Chen Zhen",
                    "Yue Minjun", "Liu Wei", "Liu Ye", "Wang Yidong", "Xia Junna", "Zhu Peihong", "Wang Yin", "Yue Minjun", "Feng Zhengjie",
                    "Zhang Dali", "Xu Lei", "He Duoling", "Li Shan", "Xue Song", "Fang Shaolin", "Song Dong", "Zhang Xiaogang", "Wang Guangyi",
                    "Ding Yi", "Zhang Huan", "Huang Rui", "Wang Guangyi", "Zhou Chunya", "Xiao Yu", "Qiu Zhijie", "Liu Jianhua", "Shen Fan",
                    "Shi Xinning", "Zhang Peili", "Liang Shaoji", "Huang Yan", "Wang Luyan", "Wang Jianwei", "Wu Shanzhuan", "Qiu Xiaofei",
                    "Liang Quan", "Xie Nanxing", "Yang Fudong", "Xu Zhen", "Geng Jianyi", "Zhan Wang", "Wang Xingwei", "Li Shan", "Chen Wenbo",
                    "Xu Bing", "Luo Zhongli", "Fang Lijun", "Xu Bing", "Shi Xinning", "Ding Yi", "Yang Shaobin", "Yang Fudong", "Jin Feng",
                    "Xue Song", "Wu Jian'an", "Mao Xuhui", "Cai Guoqiang", "Zhang Dali", "Chen Shaoxiong", "Zhou Jirong", "Wang Jianwei",
                ],
                "tags": [
                    "diseño gráfico", "diseño web", "ilustración", "arte digital", "escultura", "pintura al óleo", "acrílico", "acuarela",
                    "técnica mixta", "lienzo", "papel", "pincel", "paleta", "estudio de arte", "creatividad", "expresión artística",
                    "composición visual", "color", "textura", "técnica artística", "arte contemporáneo", "movimiento artístico",
                    "abstracción", "realismo", "impresionismo", "arte conceptual", "instalación artística", "exposición de arte",
                    "galería de arte", "obra maestra", "vanguardia artística", "retrospectiva artística", "paleta de colores",
                    "iluminación artística", "boceto artístico", "dibujo a lápiz", "dibujo a tinta", "pintura al aire libre",
                    "dibujo en carboncillo", "dibujo en pastel", "dibujo en grafito", "dibujo en tiza", "dibujo de retrato",
                    "dibujo de paisaje", "técnicas de pintura", "arte en lienzo", "arte en papel", "arte en madera",
                    "arte en metal", "arte en cerámica", "arte en vidrio", "arte en textiles", "técnicas de escultura",
                    "escultura en mármol", "escultura en bronce", "escultura en madera", "escultura en piedra",
                    "escultura en metal", "escultura en cerámica", "arte digital en 2D", "arte digital en 3D",
                    "diseño de logotipo", "identidad visual", "diseño editorial", "diseño de carteles", "ilustración digital",
                    "ilustración editorial", "ilustración infantil", "tipografía creativa", "diseño de personajes",
                    "diseño de carteles", "diseño de envases", "diseño de branding", "diseño de publicidad",
                    "software de diseño gráfico", "herramientas de diseño", "arte mural", "arte callejero",
                    "arte público", "performance art", "arte interactivo", "instalación efímera", "arte cinético",
                    "arte efímero", "arte ambiental", "arte conceptual", "arte abstracto", "arte figurativo",
                    "composición artística", "técnica de pintura", "obras de arte", "obras de gran formato",
                    "arte experimental", "arte tridimensional", "arte multimedia", "arte clásico", "arte moderno",
                    "arte contemporáneo", "galerista de arte", "comunidad artística", "museo de arte",
                    "obras de arte únicas", "subasta de arte", "colección de arte", "galería de arte en línea",
                    "artista emergente", "obras de arte originales", "comisión artística", "diseño gráfico de vanguardia",
                    "diseño de sitios web", "arte digital en la era digital", "ilustración en la era digital", "escultura en la era digital",
                    "pintura en la era digital", "arte digital en la nube", "arte tradicional vs. arte digital", "técnicas de dibujo",
                    "pintura al aire libre", "técnicas de impresión", "arte sostenible", "arte eco-friendly", "surrealismo", "cubismo",
                    "arte pop", "hiperrealismo", "fauvismo", "simbolismo artístico", "arte simbólico", "arte de la abstracción geométrica",
                    "arte de la abstracción lírica", "arte conceptual contemporáneo", "realismo mágico en el arte", "minimalismo",
                    "arte psicodélico", "arte urbano contemporáneo", "feminismo en el arte", "arte político", "arte social",
                    "arte medioambiental", "arte biomorfico", "arte postmoderno", "nuevos medios artísticos", "arte en la era de la tecnología",
                    "digitalización del arte", "tecnología en el arte contemporáneo", "arte y cultura", "impacto social del arte",
                    "arte y cambio social", "colaboración artística", "diversidad en el arte", "arte y tecnología", "intersección del arte y la ciencia"
                ],
                "elements": [
                    "people", "portrait", "model", "celebrity", "child", "adult", "elderly", "man", "woman", "couple", "group",
                    "animal", "pets", "wildlife", "bird", "mammal", "reptile", "insect", "fish",
                    "nature", "landscape", "tree", "flower", "plant", "sky", "clouds", "sun", "moon", "stars", "rainbow",
                    "architecture", "building", "house", "skyscraper", "bridge", "church", "castle", "ruins",
                    "food", "meal", "restaurant", "dish", "dessert", "drink", "coffee", "wine", "cocktail",
                    "travel", "destination", "cityscape", "street", "road", "beach", "mountain", "lake", "river", "ocean", "island", "countryside",
                    "vehicle", "car", "bike", "motorcycle", "bus", "train", "airplane", "boat", "subway", "helicopter",
                    "event", "wedding", "party", "concert", "festival", "sporting event", "conference", "parade",
                    "fashion", "clothing", "accessories", "shoes", "jewelry", "makeup", "hairstyle",
                    "technology", "computer", "smartphone", "camera", "drone", "gadget", "robot",
                    "art", "sculpture", "painting", "music", "instrument", "dance", "theater",
                    "books", "reading", "library", "study", "writing", "pen", "notebook",
                    "work", "office", "meeting", "workplace", "tools", "equipment", "construction",
                    "adventure", "exploration", "journey", "discovery", "hiking", "camping",
                    "industry", "factory", "manufacturing", "construction", "technology",
                    "health", "medical", "hospital", "doctor", "nurse", "patient",
                    "education", "school", "classroom", "learning", "student", "teacher",
                    "family", "parenting", "children", "relationship", "love", "friendship",
                    "community", "people", "diversity", "culture", "celebration", "holiday", "tradition", "festive"
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

    def get_prompts(self):
        file = 'tuning' + "/" + self.roles_tuning[self.role]["file"] + ".jsonl"

        role_description = self.roles_tuning[self.role]["description"]

        # Escena, autor y etiqueta
        scene = random.choice(self.roles_tuning[self.role]["scenes"])
        author = random.choice(self.roles_tuning[self.role]["authors"])
        tags = random.choice(self.roles_tuning[self.role]["tags"])
        element = random.choice(self.roles_tuning[self.role]["elements"])

        first_prompt = f"{role_description} similar to the author \"{author}\" . Generate me a json that contains the fields: title, description, metatags. You should focus on describing this scene: {scene}. In the described scene, this element should appear: {element}. Some tags to keep in mind when describing the title and scene: {tags}. The title should be a few words (between 7 and 25 words) and oncise. The description should be moderately detailed and contain between 40 and 400 characters in plain text. The metatags will be a comma-separated list with a maximum of 10 words containing the most relevant information for the content described. The response cannot contain anything other than a json object. The json content must be in English."


        additional_text = f"The content must adapt to the following description, Type of scene: {scene}. Work similar to those of the author suggestion: {author}. You must include these tags in the description: {tags}. Must include: {element}."

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
            print(f"scene: {scene}")
            print(f"author: {author}")
            print(f"tags: {tags}")
            print(f"element: {element}")
            print("")

        return prompts
