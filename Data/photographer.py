#! /usr/bin/env python

def getData():
    return {
        "description": "Put yourself in the role of a professional photographer",
        "file": "photographer", ## Archivo dentro del directorio "tuning"
        "params": { # Parámetros para configurar las peticiones api a Stable Diffusion
            #"model": "realistic_vision_v3.0_q6p_q8p.ckpt",
            "model": "realistic_vision__v5_f16.ckpt",
            "steps": 60,
            "cfg_scale": 4,
            "denoising_strength": 0.4,
            "sampler_index": "DPM++ 2M Karras",
            "restore_faces": False,
            "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,signature, signed, letters, text",
        },
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
        ],
        #"renders": [
        #    '–ar 16:9', "4k", "8k", "f10", "ISO 100", "200mm", "-ar 3:2", "-uplight", "-v 4", "-q 4", "-c 60", "--q 5", "hdr"
        #],
    }
