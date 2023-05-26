#!/usr/bin/env python

"""
ask_gpt.py:
    ask somthing to chatgpt
"""

import openai

def ask_gpt(input_user, log_file):
    response = openai.Completion.create(
        # text-davinci-002 sert à la génération de texte
        engine="text-davinci-003",
        # input_user sert à la input_user posée
        prompt=input_user,
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

    log_file.write("input_user: " + input_user + "\n")
    log_file.write("Réponse: " + answer + "\n\n")
    
    return answer

