#! /usr/bin/env python

def getData():
    return {
        "description": "Put yourself in the role of a professional photographer",
        "file": "photographer", ## Archivo dentro del directorio "tuning"
        "params": { # Parámetros para configurar las peticiones api a Stable Diffusion
            "model": "realistic_vision_v3.0_q6p_q8p.ckpt",
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

        ],
        "elements": [

        ]
    }
