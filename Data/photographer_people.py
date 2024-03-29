#! /usr/bin/env python

def getData():
    return {
        "description": "Put yourself in the role of a professional photographer dedicated to taking portraits of people. You will describe the scene and the person portrayed.",
        "file": "photographer_people", ## Archivo dentro del directorio "tuning"
        "params": { # Parámetros para configurar las peticiones api a Stable Diffusion
            #"model": "realistic_vision_v3.0_q6p_q8p.ckpt",
            "model": "realistic_vision__v5_f16.ckpt",
            "steps": 50,
            "cfg_scale": 3.5,
            "clip_skip": 1,
            "denoising_strength": 0.4,
            "sampler_index": "DPM++ 2M Karras",
            "restore_faces": False,
            "before_prompt": "A beautiful DSLR portrait photography",
            "negative_prompt": "nudes, naked, naked woman, naked man, lowres, signs, memes, labels, text, error, mutant, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, made by children, caricature, ugly, boring, sketch, lacklustre, repetitive, (long neck), facebook, youtube, body horror, out of frame, mutilated, tiled, frame, border, porcelain skin, doll like, doll, deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, cartoon, drawing, anime, duplicate, morbid, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, tiling, poorly drawn feet, out of frame, bad anatomy, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, draft, grainy, crayon, graphite, impressionist, noisy, soft, deformed, low quality, lowres, grayscale, worstquality, out of focus, bad body, (fat:1.2), mutated, skin blemishes, skin spots, acnes, missing limb, floating limbs, disconnected limbs, extra limb, bad hands, missing fingers, bad feet, cross-eyed, AS-YoungV2-neg, BadDream, badhandv4, BadNegAnatomyV1-neg, EasyNegative, FastNegativeV2, (distorted, :1.3), (:1.4), paintings, sketches, abstract, glitch, umbrella, raincoat, brassierre, see-through, bad, immature, graphic",
            "extra_prompt": "(detailed face:1.5), (detailed clothes:1.4), (extremely detailed eyes and face), Paparazzi Photography, foreground, detailed face, perfect mouth, photography, highly detailed, sharp focus, stunningly beautiful, 4k, 8k, HDR, UHD, high quality photography, high detailed skin, (full body:1.5), (only one person:1.6), (close up camera:1.5), (character centered in the image:1.4)"
        },
        "lora": [
            "", "mdjrny-v4", "shukezouma", "arcane style", "hiqcgbody", "crazy face", "analog", "ajaws",
        ],
        "scenes": [
            "Urban park", "Cozy café", "Sunny beach", "Art studio", "Busy street", "Peaceful forest",
            "City at night", "Beach at sunset", "Interior of a home", "Cobblestone streets", "Field of flowers",
            "Rooftop with panoramic view", "Train station", "Street market", "Botanical garden", "Antique theater",
            "Subway station", "Shopping mall", "Harbor waterfront", "Snowy mountain", "Inside of a car",
            "Gym", "Concert stage", "Quiet library", "Recording studio", "Fire station",
            "Amusement park", "Home kitchen", "Modern office", "Forest campsite", "Hiking trail",
            "Historic staircases", "Bohemian neighborhood", "Moving train", "Tropical pool", "Abandoned factory",
            "Open-air bar", "Zen garden", "Busy airport", "Rural farm", "Industrial warehouse", "Playground",
            "Medical clinic", "Dance studio", "Ski resort", "Horse farm", "Elementary school", "Yoga studio",
            "Nightclub", "Playground", "Olympic pool", "Tattoo studio", "Iconic bridge", "Vast natural park",
            "Historic city square", "Rustic barn", "Lakeside dock", "College campus", "Vineyard", "Urban graffiti wall",
            "Country road", "Botanical greenhouse", "Art gallery", "Seaside cliffs", "Mountain peak", "Quaint bookstore",
            "Music venue", "Historic mansion", "Vintage diner", "Industrial loft", "Classic theater lobby", "Small-town diner",
            "Modern architecture", "Historic library", "Peaceful pond", "Futuristic urban landscape", "Artistic mural wall",
            "Picturesque waterfall", "Ethnic market", "Highland plateau", "Historic cemetery", "Backyard garden", "Quaint village square",
            "University campus", "Secluded forest glade", "Rural railway tracks", "Lively street festival", "Waterfront marina",
            "Underground urban tunnel", "Rooftop garden", "Antique shop", "Underwater scenery", "Gleaming city skyline",
            "Boat on serene lake", "Farmers market", "Desert oasis", "Bustling food market", "Botanical arboretum",
            "Elegant ballroom", "Gothic cathedral", "Funky urban art studio", "Historic pier", "Artificial intelligence lab",
            "Vintage fashion boutique", "Quirky record store", "Lush vineyard estate", "Scenic vineyard", "Public transportation hub",
            "Vintage library", "Bookstore café", "Lively carnival", "Historic lighthouse", "Busy marketplace", "Library reading nook",
            "Antique theatre stage", "Rural farmstead", "Graffiti-covered walls", "Artistic workshop", "Victorian garden", "Charming lakeside cabin",
            "Elegant hotel lobby", "Sandy beach dunes", "Rural country fair", "Surreal abstract space", "Ballet studio", "Vintage cinema lobby",
            "Artistic alleyway", "Botanical conservatory", "Underwater cave", "Astronomical observatory", "Vivid underwater coral reef",
            "Lively rooftop party", "Artistic workshop", "Ethereal forest glen", "Historical courtroom", "Classic opera house", "Vibrant carnival parade",
            "Avant-garde fashion studio", "Rustic mountain lodge", "Medieval castle courtyard", "Victorian-era greenhouse", "Boutique perfume shop", "Artificial intelligence lab",
            "Cosmic space station", "Contemporary art festival", "Eccentric antique shop", "Retro arcade", "Luxury yacht deck", "Fairy tale forest glade", "sitting outside restaurant"
        ],
        "authors": [
            "Annie Leibovitz", "Richard Avedon", "Diane Arbus", "Irving Penn", "Steve McCurry",
            "Yousuf Karsh", "Henri Cartier-Bresson", "Nan Goldin", "Dorothea Lange", "Helmut Newton",
            "Cindy Sherman", "Robert Mapplethorpe", "Sebastião Salgado", "Mario Testino", "Elliot Erwitt",
            "Lee Jeffries", "Platon", "Mary Ellen Mark", "Albert Watson", "Sally Mann",
            "Gordon Parks", "Robert Frank", "Anton Corbijn", "Edward Steichen", "Vivian Maier",
            "Rineke Dijkstra", "Alec Soth", "Raghu Rai", "Philip-Lorca diCorcia", "David LaChapelle",
            "Rene Burri", "David Bailey", "Avedon", "Lorna Simpson", "Carrie Mae Weems",
            "August Sander", "Duane Michals", "Brigitte Lacombe", "Arja Hyytiäinen", "Nadav Kander",
            "Gisele Freund", "Mary McCartney", "Alex Prager", "Clifford Coffin", "Taryn Simon",
            "Ralph Gibson", "Larry Fink", "Lee Friedlander", "Eugene Richards", "Bruce Gilden",
            "Gisele Freund", "Gregory Crewdson", "William Wegman", "Alex Webb", "Mary Ellen Mark",
            "Nigel Parry", "Herb Ritts", "Lee Miller", "Saul Leiter", "André Kertész",
            "Ara Güler", "Jocelyn Lee", "Francesca Woodman", "Edward Weston", "Lillian Bassman",
            "Duane Michals", "Edward Curtis", "Lisette Model", "Thomas Ruff", "Ralph Gibson",
            "Alberto Korda", "Bernd Becher", "Hans Bellmer", "László Moholy-Nagy", "Duane Michals",
            "Zoe Strauss", "Saul Leiter", "Adele Enersen", "Helen Levitt", "Peter Lindbergh",
            "Man Ray", "Bert Stern", "Weegee", "Paul Strand", "Brassai",
            "Louise Dahl-Wolfe", "Bruce Weber", "Sandro Miller", "Boushra Almutawakel", "Mike Disfarmer",
            "Kwame Brathwaite", "Chris Rainier", "Astrid Kirchherr", "Jerry Schatzberg", "Kwaku Alston",
            "Moneta Sleet Jr.", "Matt Stuart", "Seb Janiak", "Paul Outerbridge", "Tina Modotti",
            "Peter Hurley", "Mark Seliger", "Herb Ritts", "Nick Knight", "Nan Goldin",
            "Gilles Bensimon", "Bruce Gilden", "Platon", "Sølve Sundsbø", "Garry Winogrand",
            "Mary McCartney", "Diane Arbus", "Tim Walker", "Dora Maar", "Inez van Lamsweerde",
            "Vincent Peters", "David LaChapelle", "Martin Schoeller", "William Klein", "Dan Winters",
            "Eve Arnold", "Nigel Parry", "David Bailey", "Jim Goldberg", "David Hilliard",
            "Zanele Muholi", "Catherine Opie", "Peter Lindbergh", "Toni Frissell", "Elliott Erwitt",
            "Jan Saudek", "Eugene Richards", "Nikki S. Lee", "Irving Penn", "Lola Álvarez Bravo",
            "LaToya Ruby Frazier", "Thomas Struth", "Lise Sarfati", "Teju Cole", "Caroline Knopf",
            "Mary Ellen Mark", "Helmut Newton", "Edward Curtis", "Dawoud Bey", "David LaChapelle",
            "Man Ray", "Bert Stern", "Weegee", "Paul Strand", "Brassai", "Louise Dahl-Wolfe",
            "Bruce Weber", "William Klein", "Dora Maar", "Toni Frissell", "Dan Winters",
            "Eve Arnold", "Jock Sturges", "Harry Callahan", "Francesca Woodman", "Graciela Iturbide",
            "Roni Horn", "David Hockney", "Andreas Gursky", "Nadav Kander", "Erwin Olaf",
            "Elinor Carucci", "Lois Conner", "Ren Hang", "Gordon Parks", "David Guttenfelder",
            "Laura Zalenga", "Kelli Connell", "Pierre Gonnord", "Phil Borges", "Wang Qingsong",
            "Susan Meiselas", "Willie Doherty", "Edward Burtynsky", "Tom Hunter", "Rineke Dijkstra",
            "Alec Soth", "Philip-Lorca diCorcia", "Tina Barney", "Lee Friedlander", "Mark Cohen",
            "Jim Dow", "Wendy Ewald", "Larry Fink", "David Hilliard", "Ken Light", "Nathan Lyons",
            "Sally Mann", "Ralph Eugene Meatyard", "Richard Misrach", "Duane Michals", "Nicholas Nixon",
            "Martin Parr", "Susan Paulson", "Lucas Samaras", "Catherine Wagner", "Andy Warhol",
            "Garry Winogrand", "Peter A. Juley & Son", "Cecil Beaton", "Yousef Karsh", "Robert Mapplethorpe",
            "Edward Steichen", "Léon Levinstein", "Danny Lyon", "Constantine Manos", "Robert Adams",
            "Berenice Abbott", "Eugène Atget", "Jules Aarons", "Jacob Riis", "Tina Modotti", "Arnold Newman",
            "Lewis W. Hine", "Aaron Siskind", "Clarence John Laughlin", "Weegee", "William Albert Allard",
            "W. Eugene Smith", "Paul Caponigro", "Karl Blossfeldt", "William Henry Fox Talbot", "Bill Brandt",
            "Eudora Welty", "Paul Outerbridge", "Man Ray", "Louise Nevelson", "Edward Weston", "Gyula Halász",
            "Lisette Model", "Clyde Butcher", "Wendy Ewald", "Roger Fenton", "Julia Margaret",
        ],
        "tags": [
            "Emotion", "Facial Expression", "Black and White Portrait", "Color Portrait", "Lighting", "Shading",
            "Skin Texture", "Gaze", "Pose", "Composition", "Background", "Contrast", "Clarity", "Skin Tone", "Focus",
            "Background Blur", "Portrait Style", "Environmental Portrait", "Studio Portrait", "Outdoor Portrait",
            "Full-Body Portrait", "Group Portrait", "Child Portrait", "Adult Portrait",
            "Elderly Portrait","Fashion Portrait", "Classic Portrait", "Contemporary Portrait",
            "Conceptual Portrait", "Celebrity Portrait", "Friend Portrait", "Family Portrait",
            "Couple Portrait", "Teen Portrait", "Model Portrait", "Musician Portrait",
            "Actor Portrait", "Artist Portrait", "Athlete Portrait", "Politician Portrait", "Executive Portrait",
            "Public Figure Portrait", "Stranger Portrait", "Everyday Life Portrait", "Traveler Portrait", "Street Portrait",
            "Documentary Portrait", "Community Portrait", "Subculture Portrait", "Minority Portrait", "Diversity Portrait",
            "Gender Portrait", "Aging Portrait", "Youth Portrait", "Beauty Portrait", "Imperfection Portrait",
            "Expression Portrait", "Personality Portrait", "Individuality Portrait", "Intimacy Portrait", "Nostalgia Portrait",
            "Emotion Portrait", "Smile Portrait", "Seriousness Portrait", "Joy Portrait", "Sadness Portrait",
            "Surprise Portrait", "Intrigue Portrait", "Confidence Portrait", "Vulnerability Portrait", "Deep Gaze Portrait",
            "Attitude Portrait", "Elegance Portrait", "Eccentricity Portrait", "Shyness Portrait", "Courage Portrait",
            "Passion Portrait", "Calmness Portrait", "Energy Portrait", "Introspection Portrait", "Mystery Portrait",
            "Wisdom Portrait", "Creativity Portrait", "Innovation Portrait", "Tradition Portrait", "Modernity Portrait",
            "Cultural Diversity Portrait", "Inclusion Portrait", "Authenticity Portrait", "Resilience Portrait",
            "Struggle Portrait", "Peace Portrait", "Equality Portrait", "Individuality Portrait", "Community Portrait",
            "Unity Portrait", "Hope Portrait", "Adversity Portrait", "Overcoming Portrait", "Happiness Portrait",
            "Sadness Portrait", "Life Portrait", "Death Portrait", "Vintage Portrait", "Modern Portrait",
            "Retro Portrait", "Contemporary Portrait", "High-Contrast Portrait", "Monochrome Portrait",
            "Candid Portrait", "Posed Portrait", "Outdoor Portrait", "Indoor Portrait", "Natural Light Portrait",
            "Studio Light Portrait", "Fine Art Portrait", "Corporate Portrait", "Urban Portrait", "Rural Portrait",
            "Dramatic Portrait", "Formal Portrait", "Casual Portrait", "Headshot", "Family Portrait",
            "Group Portrait", "Teenage Portrait", "Elderly Portrait", "Engagement Portrait",
            "Wedding Portrait", "Maternity Portrait", "Newborn Portrait", "Parent-Child Portrait", "Sibling Portrait",
            "Solo Portrait", "Dynamic Portrait", "Emotive Portrait", "Storytelling Portrait", "Fashion Editorial Portrait",
            "Beauty Portrait", "Lifestyle Portrait", "Creative Portrait", "Experimental Portrait", "Abstract Portrait",
            "Minimalist Portrait", "Maximalist Portrait", "Vintage Style Portrait", "Avant-Garde Portrait",
            "Nonconformist Portrait", "Conceptual Portrait", "Fantasy Portrait", "Whimsical Portrait", "Digital Portrait",
            "Analog Portrait", "Self-Portrait", "Narrative Portrait", "Celebrity Portrait", "Character Portrait",
            "Realistic Portrait", "Surreal Portrait", "Impressionist Portrait", "Expressionist Portrait",
            "Diverse Portrait", "Inclusive Portrait", "Intimate Portrait", "Public Portrait", "Private Portrait",
            "Powerful Portrait", "Vulnerable Portrait", "Intriguing Portrait", "Confident Portrait", "Timid Portrait",
            "Courageous Portrait", "Passionate Portrait", "Calm Portrait", "Energetic Portrait", "Reflective Portrait",
            "Enigmatic Portrait", "Wise Portrait", "Creative Process Portrait", "Innovative Portrait",
            "Traditional Portrait", "Contemporary Art Portrait", "Cultural Portrait", "Societal Portrait",
            "Environmental Portrait", "Political Portrait", "Artistic Statement Portrait", "Historical Portrait",
            "Timeless Portrait", "Progressive Portrait", "Emotional Portrait", "Inspirational Portrait", "Story of Life Portrait",
            "Natural Beauty Portrait", "Individual Portrait", "Collective Portrait", "Harmonious Portrait", "Hopeful Portrait",
            "Challenging Portrait", "Resilient Portrait", "Artistic Struggle Portrait", "Peaceful Portrait", "Equal Portrait",
            "Diverse Identity Portrait", "Humanity Portrait", "Artistic Experiment Portrait", "Mystery of Life Portrait",
            "Human Connection Portrait", "Emotion Through Time", "Emotion Through Space", "Emotion Through Time and Space", "cinematic", "sci-fi", "stunningly beautiful", "dystopian", "iridescent gold", "cinematic lighting", "dark", "highlight hair", "detailed eyes", "sharp focus", "young face", "perfect symmetric face", "pupil" "reflecting surroundings", "realistic skin", "soft healthy skin", "full body", "smoking vape",
        ],
        "elements": [
            "People", "Model", "Celebrity", "Elderly", "Man", "Woman", "Couple", "Group",
            "Friendship", "Love", "Family", "Emotion", "Expression", "Style", "Fashion", "Accessories", "Beauty",
            "Personality", "Diversity", "Individuality", "Happiness", "Sadness", "Confidence", "Vulnerability",
            "Natural Beauty", "Cultural Diversity", "Intimacy", "Public Figure", "Stranger", "Everyday Life",
            "Traveler", "Street", "Documentary", "Community", "Subculture", "Minority", "Gender", "Aging",
            "Youth", "Portraiture", "Profile", "Close-Up", "Gaze", "Gesture", "Embrace", "Laughter", "Tears",
            "Hug", "Kiss", "Interaction", "Connection", "Relationship", "Bond", "Siblings", "Parents", "Children",
            "Grandparents", "Friends", "Lovers", "Spouse", "Soulmates", "Squad", "Ethnicity", "Culture", "Tradition",
            "Lifestyle", "Character", "Expression", "Mood", "Attire", "Elegance", "Individualism", "Societal Roles",
            "Belonging", "Togetherness", "Identity", "Identity Exploration", "Personhood", "Life Stages", "Personification",
            "Narrative", "Storytelling", "Timelessness", "Historical Context", "Modern Times", "Contemporary Life",
            "Symbolism", "Contrast", "Harmony", "Uniqueness", "Resilience", "Inclusivity", "Diversity of Experience",
            "Human Essence", "Unity in Diversity", "Expression Through Portraiture", "Social and Cultural Insight",
            "Celebration of Life", "Artistic Expression", "Reflection of Humanity", "Person of Interest", "Character Study",
            "Age Diversity", "Generations", "Generational Portrait", "Religious Identity", "Cultural Pride", "Subcultural Identity",
            "Cultural Traditions", "Modern Lifestyle", "Historical Reflection", "Character Depth", "Candid Moments", "Historical Resonance",
            "Intersectionality", "Ethnic Heritage", "Cultural Heritage", "National Identity", "Transcultural Identity",
            "Social Commentary", "Elderly Wisdom", "Youthful Energy", "Generation Gap", "Social Harmony", "Cultural Fusion",
            "Gender Identity", "Gender Fluidity", "Gender Roles", "Cultural Heritage", "Gender Expression", "Ageless Beauty",
            "Cultural Integration", "Global Society", "Cross-Cultural Connections", "Cultural Exchange", "Personal Identity",
            "Cross-Generational Bonding", "Cultural Adaptation", "Personal Storytelling", "Socioeconomic Diversity",
            "Urban Lifestyle", "Rural Lifestyle", "Diverse Styles", "Socioeconomic Contrast", "Lived Experiences",
            "Human Connection", "People and Places", "Cultural Significance", "Cultural Melting Pot", "Interconnected Lives",
            "Interpersonal Relations", "Lived Realities", "Expressive Faces", "Authentic Emotions", "Identity Exploration",
            "Identity Reflection", "Social Insight", "Cultural Exploration", "Unity in Expression", "Expressive Character",
            "Emotional Portrayal", "Intimate Moments", "Human Bonding", "Cultural Diversity Portrait", "Life Journeys",
            "Relational Portraiture", "Life Stories", "Cultural Richness", "Personal Expression", "Identity Through Time",
            "Individual Experiences", "Emotion Through Portraits", "Social and Cultural Significance", "Lifelong Memories",
            "Cultural Narratives", "Personal Narratives", "Cultural Experience", "Shared Experiences", "Socioeconomic Realities",
            "Cultural Identity", "Interpersonal Connections", "Cultural Unity", "Harmony in Diversity", "Personal Truths",
            "Universal Emotions", "Cultural Celebrations", "Mosaic of Humanity", "Cultural Traditions", "Generational Wisdom",
            "Cultural Ancestry", "Respect for Age", "Youthful Enthusiasm", "Historical Insight", "Contemporary Insights",
            "Cultural Legacy", "Gender Equality", "Diverse Voices", "Shared Emotions", "Interconnected Stories", "Collective Experience",
            "Culture and Society", "Human Resilience", "Emotionally Resonant Portraits", "Socioeconomic Reflections", "Interwoven Lives", "young female", "blue eyes", "highlights in hair", "wearing a white outfit", "side light",
            "olive green eyes", "green eyes"
        ],
        "renders": [
            "Canon EOS 5D Mark IV",
            "Canon EOS-1D X Mark III",
            "Canon EOS R5",
            "Nikon D850",
            "Nikon Z7",
            "Nikon D6",
            "Sony Alpha a7R IV",
            "Sony Alpha a9 II",
            "Sony Alpha 1",
            "Fujifilm X-T4",
            "Fujifilm GFX 100S",
            "Fujifilm X-Pro3",
            "Panasonic Lumix S1R",
            "Panasonic Lumix S5",
            "Panasonic Lumix GH5",
            "Leica M10-R",
            "Leica SL2",
            "Leica Q2",
            "Hasselblad X1D II 50C",
            "Hasselblad H6D-400c MS",
            "Hasselblad 907X 50C",
            "Phase One XF IQ4 150MP",
            "Phase One XT IQ4 150MP"
        ]
        #"renders": [
        #    "50mm", "85mm", "100mm", "-ar 3:2", '–ar 16:9', "4k", "8k", "-ar 2:3", "-v 4", "180mm", "--uplight", "–uplight –v 4 –q 4", "16mm Lens, 32k --ar 16:9", "100mm", "studio lighting", "--q 2 --s 50", "hdr"
        #],
    }
