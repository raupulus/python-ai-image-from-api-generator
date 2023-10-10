#! /usr/bin/env python
def getData():
    return {
        "description": "Put yourself in the role of an artist who designs monsters, already invented mythological and legendary beings such as dragons, ogres, devils, demons, yeti, aliens, giant spiders, dinosaurs... but also creates new beings",
        "file": "artist_monster", ## Archivo dentro del directorio "tuning"
        "params": { # Parámetros para configurar las peticiones api a Stable Diffusion
            #"model": "sd_v2.1_768_v_f16.ckpt",
            #"model": "realistic_vision_v3.0_q6p_q8p.ckpt",
            "model": "realistic_vision__v5_f16.ckpt",
            "steps": 50,
            "cfg_scale": 3,
            "denoising_strength": 1,
            #"sampler_index": "Euler a",
            "sampler_index": "DPM++ 2M Karras",
            "restore_faces": False,
            "negative_prompt": "signature, signed, letters, text",
        },
        "scenes": [
            "cave", "forest", "mountain", "underground cave", "underwater cave", "abyss", "desert", "swamp", "ruined city",
            "abandoned building", "haunted house", "dark alley", "crypt", "graveyard", "jungle", "volcano", "underground tunnel",
            "deep sea", "space", "alien planet", "moon surface", "haunted forest", "enchanted forest", "foggy moor", "ancient ruins",
            "shipwreck", "castle", "dark dungeon", "wasteland", "underground lair", "spirit world", "dreamscape", "time vortex",
            "fairy tale kingdom", "cursed island", "magic portal", "hellish landscape", "celestial realm", "floating islands",
            "dark dimension", "village in peril", "abandoned laboratory", "post-apocalyptic city", "swirling tornado",
            "prehistoric jungle", "hidden cave system", "enchanted lake", "mystical temple", "extraterrestrial spacecraft",
            "underground city", "crystal cavern", "underwater palace", "underground forest", "haunted ship", "dystopian future",
            "enchanted garden", "steampunk city", "demonic realm", "frozen wasteland", "enchanted castle", "alien invasion",
            "wizards' tower", "underwater abyss", "ghost ship", "flying saucer", "enchanted waterfall", "cursed village",
            "underwater city", "ancient library", "interdimensional rift", "nightmare realm", "underground river", "forgotten temple",
            "haunted hospital", "sunken ship", "enchanted cave", "enchanted island", "ancient battleground", "dark forest clearing",
            "enchanted pond", "ancient tree grove", "haunted mansion", "underground maze", "wizards' academy", "enchanted market",
            "enchanted forest glade", "surreal dreamland", "enchanted labyrinth", "underground kingdom", "enchanted waterfall",
            "demonic castle", "futuristic cityscape", "enchanted village", "enchanted castle ruins", "underground lake",
            "enchanted mountain peak", "alien landscape", "underwater shipwreck", "enchanted forest stream", "haunted amusement park",
            "underground catacombs", "enchanted floating city", "alien forest", "enchanted underground garden",
            "ancient sacrificial altar", "enchanted underwater grotto", "time-traveling portal", "enchanted hidden glen",
            "enchanted forest canopy", "underground crystal mine", "enchanted waterfall cave", "demonic throne room",
            "enchanted underwater world", "enchanted floating island", "haunted theater", "enchanted forest waterfall",
            "alien research facility", "enchanted mountain pass", "underground chasm", "enchanted forest clearing",
            "post-apocalyptic wasteland", "enchanted forest bridge", "haunted asylum", "enchanted underwater coral reef"
        ],
        "authors": [
            "H.P. Lovecraft", "Clive Barker", "Guillermo del Toro", "Neil Gaiman", "Stephen King", "Anne Rice", "Mary Shelley",
            "Bram Stoker", "J.K. Rowling", "Terry Pratchett", "C.S. Lewis", "George R.R. Martin", "Philip Pullman", "J.R.R. Tolkien",
            "Suzanne Collins", "Rick Riordan", "Patrick Ness", "Octavia E. Butler", "China Miéville", "Ray Bradbury", "Isaac Asimov",
            "Arthur C. Clarke", "Philip K. Dick", "Frank Herbert", "Stephenie Meyer", "George Orwell", "Aldous Huxley", "Kurt Vonnegut",
            "Raymond E. Feist", "Terry Brooks", "Michael Moorcock", "Robert E. Howard", "Terry Goodkind", "Jim Butcher",
            "Andrzej Sapkowski", "Jeff VanderMeer", "Mervyn Peake", "Jeffrey Ford", "Caitlín R. Kiernan", "M.R. James", "China Tom Miéville",
            "Jeff Strand", "David Wong", "Larry Correia", "Bentley Little", "David Farland", "Brett J. Talley", "Tim Curran", "Laird Barron",
            "Kat Howard", "Cassandra Khaw", "John Langan", "Helen Marshall", "Victor LaValle", "Thomas Ligotti", "Livia Llewellyn",
            "S.P. Miskowski", "Gemma Files", "Adam Nevill", "Paul Tremblay", "Sarah Pinborough", "Nick Cutter", "Josh Malerman",
            "Christopher Golden", "Brian Lumley", "Simon Clark", "Richard Laymon", "Jack Ketchum", "Graham Masterton", "Ramsey Campbell",
            "Peter Straub", "Robert McCammon", "Joe Hill", "Mark Z. Danielewski", "Jonathan Maberry", "Dan Simmons",
            "Lauren Beukes", "Joe Abercrombie", "Patrick Rothfuss", "Brandon Sanderson", "Tad Williams", "Robin Hobb", "Steven Erikson",
            "Lev Grossman", "Kazuo Ishiguro", "N.K. Jemisin", "Gene Wolfe", "Roger Zelazny", "David Gemmell", "Glen Cook",
            "Robin McKinley", "Guy Gavriel Kay", "Susanna Clarke", "Erin Morgenstern", "Terry Brooks", "Marion Zimmer Bradley",
            "Michael Ende", "Ursula K. Le Guin", "H.G. Wells", "Edgar Allan Poe", "Cassandra Clare", "Patricia A. McKillip",
            "R.A. Salvatore", "Terry Pratchett", "Piers Anthony", "Raymond E. Feist", "Terry Brooks", "Margaret Atwood",
            "Ken Follett", "Orson Scott Card", "Poul Anderson", "Larry Niven", "Nancy A. Collins", "Graham Masterton",
            "Richard Matheson", "John Ajvide Lindqvist", "Peter Benchley", "Dan Simmons", "Algernon Blackwood", "John Wyndham",
            "Clifford D. Simak", "Mikhail Bulgakov", "Josef Nesvadba", "Lucius Shepard", "James Herbert", "Richard Adams", "Leonardo DaVinci", "D&D", "Terry Richardson"
        ],
        "tags": [
            "diabolical", "sinister", "terrifying", "angelic", "dramatic", "demonic", "deformed", "impressive", "enormous",
            "gigantic", "illuminated", "mysterious", "mythical", "nightmarish", "otherworldly", "spectacular", "supernatural",
            "monstrous", "ethereal", "apocalyptic", "legendary", "grotesque", "fantastical", "epic", "sinister", "darkly beautiful",
            "malevolent", "surreal", "bewitching", "cursed", "haunting", "majestic", "vivid", "otherworldly", "mystical",
            "cataclysmic", "ferocious", "unearthly", "breathtaking", "ominous", "chimerical", "majestic", "sorcerous",
            "enigmatic", "unforgiving", "eerie", "ethereal", "enchanted", "fearsome", "spellbinding", "legendary", "grotesque",
            "timeless", "spellbound", "supernatural", "monumental", "terrifyingly beautiful", "bewildering", "enigmatic",
            "mythic", "fantasmagoric", "dreadful", "terrific", "spectacularly sinister", "spellbound", "sublime",
            "spectacularly eerie", "dreadful", "enchanting", "spellbindingly surreal", "awe-inspiring", "spellbindingly epic",
            "awe-inspiringly malevolent", "captivating", "bewilderingly fantastical", "sublimely ominous", "hauntingly ethereal",
            "elegantly maleficent", "captivatingly dark", "bewitchingly monstrous", "spellbindingly angelic", "enchantingly monstrous",
            "spellbindingly diabolic", "awe-inspiringly mysterious", "bewilderingly colossal", "majestically wicked",
            "elegantly horrifying", "captivatingly mythical", "sublimely nightmarish", "bewitchingly surreal", "sublimely bizarre",
            "spellbindingly legendary", "awe-inspiringly monstrous", "captivatingly grotesque", "hauntingly dramatic",
            "enchantingly surreal", "awe-inspiringly ethereal", "majestically demonic", "sublimely enchanting", "awe-inspiringly surreal",
            "bewilderingly grotesque", "captivatingly angelic", "spellbindingly bizarre", "sublimely ethereal", "awe-inspiringly sinister",
            "bewilderingly eerie", "majestically fantastic", "captivatingly mythic", "sublimely surreal", "hauntingly otherworldly",
            "elegantly apocalyptic", "spellbindingly otherworldly", "awe-inspiringly nightmarish", "bewilderingly angelic",
            "majestically surreal", "captivatingly malevolent", "sublimely bewitching", "awe-inspiringly enchanting",
            "elegantly spellbinding", "captivatingly monstrous", "bewilderingly nightmarish", "awe-inspiringly diabolic",
            "spellbindingly mystical", "majestically epic", "sublimely demonic", "bewilderingly ethereal", "awe-inspiringly fantastic", "artstation"
        ],
        "elements": [
            "weapons", "claws", "tentacles", "wings", "mutant", "rock", "fire", "wind", "snow", "fangs", "armor", "horns", "scales",
            "fins", "fur", "spikes", "flesh", "eyes", "teeth", "tongue", "pincers", "slime", "blood", "wounds", "chains", "crystals",
            "mists", "shadows", "light", "curses", "magic", "potions", "runes", "rituals", "scrolls", "amulets", "treasure",
            "traps", "caverns", "lairs", "castles", "temples", "portals", "abyss", "dungeons", "crypts", "haunts", "mazes", "labyrinths",
            "forests", "swamps", "jungles", "deserts", "oceans", "caves", "mountains", "islands", "skies", "moons", "planets", "stars",
            "galaxies", "void", "time", "dimensions", "realms", "worlds", "beasts", "monsters", "dragons", "demons", "angels", "zombies",
            "vampires", "werewolves", "ghosts", "spirits", "golems", "giants", "serpents", "krakens", "phoenixes", "griffins", "unicorns",
            "sirens", "chimeras", "sorcerers", "witches", "wizards", "necromancers", "shamans", "oracles", "creatures", "abominations",
            "aberrations", "horror", "mystery", "fate", "destiny", "darkness", "light", "good", "evil", "chaos", "order", "timelessness",
            "eternity", "infinity", "power", "destruction", "creation", "transformation", "ascension", "desolation", "salvation", "apocalypse",
            "tentacle monsters", "chained horrors", "fire-breathing beasts", "enchanted forests", "haunted mansions", "cryptic runes",
            "ethereal spirits", "sorcerous rituals", "monstrous abominations", "frozen wastelands", "gigantic serpents", "celestial realms",
            "demonic pacts", "cursed artifacts", "time-traveling portals", "surreal dreamscapes", "eldritch horrors", "shadowy dimensions",
            "undead hordes", "mystical tomes", "bewitched amulets", "otherworldly portals", "enchanted weapons", "mythical creatures",
            "dark sorcery", "ancient prophecies", "heroic quests", "timeless battles", "cosmic entities", "elders of the abyss", "nightmarish visions",
            "sacred relics", "underworld journeys", "forgotten civilizations", "celestial beings", "interdimensional rifts", "monstrous transformations",
            "eternal conflict", "mystical artifacts", "underwater mysteries", "shadowy conspiracies", "legendary heroes", "mythical origins",
            "ancestral curses", "ancient ruins", "cursed landscapes", "sorcerous duels", "mythical creatures", "dark prophecies", "strange phenomena",
            "cursed cities", "enchanted realms", "horrifying revelations", "cryptic symbols", "cosmic forces", "mythical relics", "enchanted woods",
            "time-worn scrolls", "arcane knowledge", "fateful choices", "ethereal landscapes", "endless quests", "monstrous adversaries",
            "time-bending artifacts", "enchanted castles", "haunting echoes", "sorcerous incantations", "legendary battles", "otherworldly beings", "tree monster"
        ],
        "renders": [
            "Pixar", "Octane", "Blender", "Arnold", "V-Ray", "Mental Ray", "Redshift", "Corona",
            "Unity", "Unreal", "Cinema 4D", "Maxwell", "KeyShot", "LuxCore",
            "bit maps", "vector graphics",
            "Substance Designer", "PBR (Physically Based Rendering)", "Global Illumination", "Ray Tracing", "Volumetric Rendering",
            "Digital Sculpting", "Procedural Generation", "UV Mapping", "Retopology", "Normal Mapping", "Bump Mapping",
            "Rigging and Animation", "Fluid Simulation", "Particle Systems", "Matte Painting", "Digital Matte Painting", "Texture Mapping",
            "2D Animation", "3D Animation", "Motion Capture", "Virtual Reality (VR)", "Augmented Reality (AR)",
            "Real-Time Rendering", "Non-Photorealistic Rendering (NPR)", "Pixel Art", "Cel Shading", "Stylized Rendering",
            "Photobashing", "Digital Painting", "Concept Art", "Storyboarding", "Character Design", "Environment Design",
            "Creature Design", "Vehicle Design", "Architectural Visualization", "Product Visualization", "Medical Visualization",
            "Scientific Visualization", "Data Visualization", "Infographics", "Illustration", "Film Production", "Visual Effects (VFX)"
        ],
    }
