#! /usr/bin/env python
import os
import json
from Models.Api import Api
import uuid

jsonInfo = {"batch_id": "1fc72c8bbe89b6219f1ef80aa71fa2f9", "ai": "Stable Diffusion", "role": "photographer_people", "title": "Exquisite Stillness Black and White Portraits in a Serene Yoga Studio", "description": "Be mesmerized by these ethereal portraits captured in a tranquil yoga studio, as your eyes and mind surrender to the serene and effortless fashion in motion Gaze upon the beauty of fluidity transposing into timeless images, in blissful harmony with the simplest of adornments", "tags": ["yoga", "studio", "black and white portrait", "fashion", "serenity", "tranquility", "fluidity", "mindfulness", "effortless", "serene"], "prompt": "Exquisite Stillness Black and White Portraits in a Serene Yoga Studio, Be mesmerized by these ethereal portraits captured in a tranquil yoga studio, as your eyes and mind surrender to the serene and effortless fashion in motion Gaze upon the beauty of fluidity transposing into timeless images, in blissful harmony with the simplest of adornments, yoga, studio, black and white portrait, fashion, serenity, tranquility, fluidity, mindfulness, effortless, serene, detailed face, perfect mouth, photography, highly detailed, sharp focus, stunningly beautiful, 8k", "size": "1024x576", "quantity": 32, "model": "realistic_vision__v5_f16.ckpt", "steps": 90, "cfg_scale": 4.5, "denoising_strength": 0.35, "sampler_index": "DPM++ SDE Karras", "restore_faces": True, "negative_prompt": "deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, blurry, draft, grainy, drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly, low quality, bad anatomy, lowres, normal quality, grayscale, worstquality, watermark, bad proportions, out of focus, username, bad body, (fat:1.2), long neck, mutated, mutation, disfigured, poorly drawn face, skin blemishes, skin spots, acnes, missing limb, malformed limbs, floating limbs, disconnected limbs, extra limb, extra arms, mutated hands, poorly drawn hands, malformed hands, mutated hands and fingers, bad hands, missing fingers, fused fingers, too many fingers, extra legs, bad feet, cross-eyed, AS-YoungV2-neg, BadDream, badhandv4, BadNegAnatomyV1-neg, EasyNegative, FastNegativeV2, (distorted, :1.3), (:1.4), paintings, sketches, monochrome, text, close up, cropped, out of frame, worst quality, jpeg artifacts, duplicate, morbid, mutilated, extra fingers, dehydrated, extra limbs, cloned face, gross proportions, missing arms, missing legs, anime, cartoon, graphic, abstract, glitch, umbrella, raincoat, brassierre, see-through", "seeds": [756958320, 3284156175, 3109596510, 1383638075, 2266924157, 3088544893, 1964149176, 1297830866, 2115121388, 664871495, 3459085786, 768027264, 1765335983, 2999105730, 3958668790, 1326330474, 307058911], "resizer": "Real-ESRGAN x4", "refiner_model": "sd_xl_refiner_1.0_f16.ckpt", "clip_skip": 2, "extra_prompt": "detailed face, perfect mouth, photography, highly detailed, sharp focus, stunningly beautiful, 8k"}

path = '/Users/fryntiz/git/python-ai-image-from-api-generator/output/2d24 - Exquisite Stillness Black and White Portraits in a Serene Yoga Studio'

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
