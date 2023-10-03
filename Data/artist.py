#! /usr/bin/env python
def getData():
    return {
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