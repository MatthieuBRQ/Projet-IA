#!/usr/bin/env python

"""
data.py:
    Data class
"""


class Data:
    def __init__(s) -> None:
        # Création/Ouverture du fichier log
        s.log_file = open("log.txt", "a")
        s.api_key = None
