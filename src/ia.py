#!/usr/bin/env python

"""
ia.py:
    ia core function
"""

import subprocess
import webbrowser

from src.loading_animation import loading_animation
from src.built_in import built_in
from src.ask_gpt import ask_gpt
from src.create_image import create_image

def ia(data):
    input_user = None

    while True:
        input_user = input("$> ")
        if (built_in(input_user, data.log_file) == 1):
            continue
        
        if (input_user in ("ouvre google", "ouvre youtube", "ouvre discord", "ouvre github", "ouvre twitter", "ouvre instagram", "ouvre facebook", "ouvre reddit")):
            print("ouverture de " + input_user.split(" ")[1])
            url = "https://www." + input_user.split(" ")[1] + ".com"
            webbrowser.open_new(url)
            continue

        if input_user.startswith("execute "):
            file_name = input_user.split(" ")[1] + ".py"
            print(f"Execution du programme {file_name}")
            loading_animation(3, "Chargement en cours : ", "■")
            subprocess.call(["python", file_name])
            continue
        
        if input_user == "crée une image":
            create_image(input("prompt image : "))
            continue

        ask_gpt(input_user, data.log_file)
