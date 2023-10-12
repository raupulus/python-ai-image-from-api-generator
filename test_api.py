#! /usr/bin/env python
import os
import json
from Models.Api import Api
import uuid

jsonInfo = {"batch_id": "23e1cc7cbc15006e92048cf188785173", "ai": "Stable Diffusion", "role": "photographer", "title": "Tsunami's Fury at the Coastline", "description": "This photograph captures a scene of unparalleled chaos as a massive tsunami engulfs the coastline. Towering waves, like liquid giants, surge towards the land, dwarfing everything in their path. The sheer force of the water creates a deafening roar, and the coastal buildings and structures are mere matchsticks in the face of nature's fury. People are fleeing in all directions, seeking higher ground to escape the impending disaster. It's a stark reminder of the overwhelming power of the ocean and the need for preparedness in the face of such catastrophic events.", "tags": ["Tsunami", "Coastline", "Natural Disaster", "Destructive Waves", "Emergency Evacuation", "Ocean's fury", "catastrophic event", "power of nature", "Disaster Preparedness", "Survival"], "prompt": "Tsunami's Fury at the Coastline, This photograph captures a scene of unparalleled chaos as a massive tsunami engulfs the coastline. Towering waves, like liquid giants, surge towards the land, dwarfing everything in their path. The sheer force of the water creates a deafening roar, and the coastal buildings and structures are mere matchsticks in the face of nature's fury. People are fleeing in all directions, seeking higher ground to escape the impending disaster. It's a stark reminder of the overwhelming power of the ocean and the need for preparedness in the face of such catastrophic events. Tsunami, Coastline, Natural Disaster, Destructive Waves, Emergency Evacuation, Ocean's fury, catastrophic event, power of nature, Disaster Preparedness, Survival", "size": "1024x576", "quantity": 32, "model": "realistic_vision__v5_f16.ckpt", "steps": 60, "cfg_scale": 4, "denoising_strength": 0.4, "sampler_index": "DPM++ 2M Karras", "restore_faces": False, "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck,signature, signed, letters, text", "seeds": [2816520856, 3219899199, 3126854955, 1486967057, 2299840468, 3968848937, 2705035030, 3278991883, 1573260400, 2672147486, 3435723278, 2045310299, 1442608740, 983850437, 141071897, 3591388729, 3821303889, 1762507898, 3435418925, 2386856620, 154948484, 2556996204, 3775075606, 2640449903, 433836357, 284351533, 225855126, 1209104039, 3241787234, 1439070083, 21806611, 3686118300], "resizer": "Real-ESRGAN x4", "refiner_model": "sd_xl_refiner_1.0_f16.ckpt"}

path = '/Users/fryntiz/git/python-ai-image-from-api-generator/output/6e07-Tsunami\'s Fury at the Coastline'

if not jsonInfo.get('ai'):
    jsonInfo['ai'] = "Stable Diffusion"

if not jsonInfo.get('batch_id'):
    jsonInfo['batch_id'] = os.urandom(16).hex()

if not jsonInfo.get('role'):
    jsonInfo['role'] = "photographer"

if jsonInfo.get('metatags'):
    jsonInfo['tags'] = jsonInfo['metatags']
    del jsonInfo['metatags']

if not jsonInfo.get('resizer'):
    jsonInfo['resizer'] = "Real-ESRGAN x4"

if not jsonInfo.get('refiner_model'):
    jsonInfo['refiner_model'] = "sd_xl_refiner_1.0_f16.ckpt"

if not jsonInfo.get('negative_prompt'):
    jsonInfo['negative_prompt'] = ""

print("")
print("")
print("ASEGÚRATE DE CAMBIAR SERVIDOR!!!! CUIDADO SUBIENDO A REAL!!!!")
print("")
print("")

exit(1)

api = Api()
api.directoryUpload(jsonInfo, path)
