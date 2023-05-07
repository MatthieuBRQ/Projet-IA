#!/usr/bin/env python

"""
ia.py:
    ia core function
"""

import openai
import subprocess
import webbrowser
import requests

from src.loading_animation import loading_animation
from src.pre_prompt import pre_prompt
from src.built_in import built_in


def ia(data):
    openai.api_key = data.api_key

    pre_prompt()

    while True:
        question = input("$> ")
        if (built_in(question, data.log_file) == 1):
            continue

        if question == "ouvre google":
            url = "https://www.google.com"
            webbrowser.open_new(url)
            print("ouverture de google")
            continue

        if question == "ouvre youtube":
            url = "https://www.youtube.com"
            webbrowser.open_new(url)
            print("ouverture de youtube")
            continue

        if question == "ouvre discord":
            url = "https://discord.com"
            webbrowser.open_new(url)
            print("ouverture de discord")
            continue

        if question == "ouvre github":
            url = "https://github.com"
            webbrowser.open_new(url)
            print("ouverture de github")
            continue

        if question == "ouvre twitter":
            url = "https://twitter.com"
            webbrowser.open_new(url)
            print("ouverture de twitter")
            continue

        if question == "ouvre instagram":
            url = "https://www.instagram.com"
            webbrowser.open_new(url)
            print("ouverture de instagram")
            continue

        if question == "ouvre facebook":
            url = "https://www.facebook.com"
            webbrowser.open_new(url)
            print("ouverture de facebook")
            continue

        if question == "ouvre reddit":
            url = "https://www.reddit.com"
            webbrowser.open_new(url)
            print("ouverture de reddit")
            continue

        if question.startswith("execute "):
            file_name = question.split(" ")[1] + ".py"
            print(f"Execution du programme {file_name}")
            loading_animation(3, "Chargement en cours : ", "■")
            subprocess.call(["python", file_name])
            continue

        if question == "crée une image":
            prompt = input("prompt image : ")
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
            continue

        response = openai.Completion.create(
            # text-davinci-002 sert à la génération de texte
            engine="text-davinci-003",
            # question sert à la question posée
            prompt=question,
            # max_tokens sert à la longueur de la réponse
            max_tokens=500,
            # n sert au nombre de réponse
            n=1,
            # stop sert à la fin de la réponse
            stop=None,
            # temperature sert à la température de la réponse
            temperature=0.7,
        )

        answer = response.choices[0].text.strip()
        print("\033[32m" + answer + "\033[0m")

        data.log_file.write("Question: " + question + "\n")
        data.log_file.write("Réponse: " + answer + "\n\n")
