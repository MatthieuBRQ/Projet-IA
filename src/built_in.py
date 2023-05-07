#!/usr/bin/env python

"""
built_in.py:
    execute built_in command
"""

from src.loading_animation import loading_animation


def built_in(question, log_file):
    if question == "exit":
        print("fermeture du programme")
        loading_animation(3, "Chargement en cours : ", "■")
        log_file.close()
        exit(0)
    if question == "clear":
        print("\033c")
        return 1
    return 0
