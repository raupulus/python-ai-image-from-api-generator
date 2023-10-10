#! /usr/bin/env python
import os
import json
from Models.Api import Api
import uuid

jsonInfo = {"ai": "Stable Diffusion", "role": "photographer", "title": "Photography of giant wolf in a forest or rock or mountain", "description": "Like National geographic wildlife photo of the year,dslr,ultra quality,8k,uhd,no text,no logo, -deformed,disfigured,underexposed overexposed", "tags": ["wolf", "wolfs", "mountain", "winter", "snow"], "prompt": "Photography of giant wolf in a forest or rock or mountain, National geographic wildlife photo of the year,dslr,ultra quality,8k,uhd,no text,no logo, -deformed,disfigured,underexposed overexposed, wolf, wolfs, mountain, winter, snow", "size": "1024x576", "quantity": 42, "model": "realistic_vision__v5_f16.ckpt", "steps": 60, "cfg_scale": 7.5, "denoising_strength": 0.7, "sampler_index": "DPM++ 2M Karras", "restore_faces": False, "negative_prompt": "signature, signed, letters, text", "seeds": [42826106,403888025,441014300,517671881,563351374,571099316,2346751768,2949542256,3111692473,2070895389,1588649455,1713252474,2278850210,2442842235,3106890641,3836670537,4277161695,307330058,969452818,359604202,487791297,618049731,1095353047,1213404679,1384894480,1994114578,2028964494,2244667273,3073096036,3236722055,3371638634,3478216219,1252449688,1575514496,2536372384,2887174829,3710472588,4242989940,263221179,684938732,788822844,830870832], "resizer": "Real-ESRGAN x4", "refiner_model": "sd_xl_refiner_1.0_f16.ckpt"}

path = '/Users/fryntiz/git/python-ai-image-from-api-generator/output/0_upload'

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

exit()

api = Api()
api.directoryUpload(jsonInfo, path)
