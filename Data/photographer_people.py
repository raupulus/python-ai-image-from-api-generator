#! /usr/bin/env python

def getData():
    return {
        "description": "Put yourself in the role of a professional photographer",
        "file": "photographer", ## Archivo dentro del directorio "tuning"
        "params": { # Parámetros para configurar las peticiones api a Stable Diffusion
            #"model": "realistic_vision_v3.0_q6p_q8p.ckpt",
            "model": "realistic_vision__v5_f16.ckpt",
            "steps": 90,
            "cfg_scale": 6,
            "denoising_strength": 0.5,
            "sampler_index": "DPM++ SDE Karras",
            "restore_faces": True,
            "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck",
        },
        "scenes": [

        ],
        "authors": [

        ],
        "tags": [
            "cinematic photography", "commercial photography", "editorial photography", "fine art photography", "wedding photography", "event photography", "cinematic light", "ultra realistic", "ultra detailed", "Photorealistic, human photography", "portrait", "ultraddetailed", "good light filter", "drinking"
        ],
        "elements": [
            "people", "model", "celebrity", "child", "adult", "elderly", "man", "woman", "couple", "group", "group peoples"
        ],
        #"renders": [
        #    "50mm", "85mm", "100mm", "-ar 3:2", '–ar 16:9', "4k", "8k", "-ar 2:3", "-v 4", "180mm", "--uplight", "–uplight –v 4 –q 4", "16mm Lens, 32k --ar 16:9", "100mm", "studio lighting", "--q 2 --s 50", "hdr"
        #],
    }
