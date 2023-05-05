import openai
import time
import subprocess
import webbrowser
import requests

openai.api_key = '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'

print("\n")

log_file = open("log.txt", "a") # Création du fichier log.txt & a sert à ajouter du texte dans le fichier

###########################################################################################################################
print("\033[31m" + "\t$$$$$___ __$$$$$$$_ ___$$$$$__ ___$$__ __$$$$$$__ __$$$$$$$_ __________$$$$_ ____$$$___" + "\033[0m")
print("\033[31m" + "\t$$__$$__ __$$______ __$$___$$_ ___$$__ __$$___$$_ __$$______ ___________$$__ ___$$_$$__" + "\033[0m")
print("\033[31m" + "\t$$___$$_ __$$$$$___ ___$$$____ _______ __$$___$$_ __$$$$$___ ___________$$__ __$$___$$_" + "\033[0m")
print("\033[31m" + "\t$$___$$_ __$$______ _____$$$__ ___$$__ __$$$$$$__ __$$______ ___________$$__ __$$$$$$$_" + "\033[0m")
print("\033[31m" + "\t$$__$$__ __$$______ __$$___$$_ ___$$__ __$$___$$_ __$$______ ___________$$__ __$$___$$_" + "\033[0m")
print("\033[31m" + "\t$$$$$___ __$$$$$$$_ ___$$$$$__ __$$$$_ __$$___$$_ __$$$$$$$_ __________$$$$_ __$$___$$_" + "\033[0m")
###########################################################################################################################

print("\n")

print("\033[31m" + "\t\t\tProjet via API OpenAI GPT-3 || by D3sir3" + "\033[0m")

print("\n")

import time

def loading_animation(seconds, message="Loading", symbol="▋"):
    print(message, end="")
    for i in range(10):
        print(symbol, end="", flush=True)
        time.sleep(seconds / 10)
    print(" Done!")

while True:
    question = input("$> ")

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
    
    if question == "exit":
        print("fermeture du programme")
        loading_animation(3, "Chargement en cours : ", "■")
        log_file.close()
        exit()

      

    if question == "clear":
        print("\033c")
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
        engine="text-davinci-003", # text-davinci-002 sert à la génération de texte
        prompt=question, # question sert à la question posée
        max_tokens=500, # max_tokens sert à la longueur de la réponse
        n=1, # n sert au nombre de réponse
        stop=None, # stop sert à la fin de la réponse
        temperature=0.7, # temperature sert à la température de la réponse
    )

    answer = response.choices[0].text.strip()
    print("\033[32m" + answer + "\033[0m")

    log_file.write("Question: " + question + "\n")
    log_file.write("Réponse: " + answer + "\n\n")
