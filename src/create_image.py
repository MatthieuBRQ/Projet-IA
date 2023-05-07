#!/usr/bin/env python

"""
create_image.py:
    create a image from a prompt
"""

import openai
import requests

from src.loading_animation import loading_animation

def create_image(prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        response = requests.get(image_url)
        loading_animation(3, "Chargement en cours : ", "■")
        with open("image.jpg", "wb") as f:
            f.write(response.content)
