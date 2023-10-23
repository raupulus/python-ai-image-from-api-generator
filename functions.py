#! /usr/bin/env python

from PIL import Image
import random
import string
import os

def image_resize(image_path, output_path, max_width = 1920, max_height = 1920):
    """
    Redimension la imagen recibida y la guarda en la ruta especificada.

    :param output_path: Ruta de la carpeta donde guardar la imagen redimensionada.
    :param image_path: Ruta de la imagen a redimensionar.
    :param max_width: Ancho máximo de la imagen redimensionada.
    :param max_height: Alto máximo de la imagen redimensionada.

    :return: Ruta de la imagen redimensionada.
    """

    # Abrir la imagen original
    image = Image.open(image_path)

    # Almaceno las dimensiones originales de la imagen
    width, height = image.size

    # Calculo la nueva dimensión manteniendo la relación de aspecto
    if width > max_width or height > max_height:
        width_related_aspect = max_width / width
        height_related_aspect = max_height / height
        related_aspect = min(width_related_aspect, height_related_aspect)

        new_width = int(width * related_aspect)
        new_height = int(height * related_aspect)

        # Redimensiono la imagen
        new_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Genero un nombre de archivo aleatorio para la imagen temporal redimensionada
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

        # Obtengo la extensión de la imagen original
        _, extension = os.path.splitext(image_path)

        # Guardo la imagen redimensionada con el nombre aleatorio y la extensión original
        new_path = os.path.join(output_path, random_name + extension)

        new_image.save(new_path)

        return new_path
    else:
        # La imagen ya cumple con las dimensiones máximas
        print('La imagen ya cumple con las dimensiones máximas.')

        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        _, extension = os.path.splitext(image_path)

        new_path = os.path.join(output_path, random_name + extension)

        image.save(new_path)

        return new_path
