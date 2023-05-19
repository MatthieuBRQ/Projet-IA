#!/usr/bin/env python

"""
pre_prompt.py:
    pre_prompt of the ai
"""

from src.ask_gpt import ask_gpt

def pre_prompt(log_file):
    with open('res/preprompt.txt', 'r') as file:
        text = file.read().replace('\n', '')
        ask_gpt(text, log_file)
