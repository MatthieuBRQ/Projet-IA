#!/usr/bin/env python

"""
loading_animation.py:
    print graphical loading progression into the terminal
"""

import time


def loading_animation(seconds, message="Loading", symbol="▋"):
    print(message, end="")
    for i in range(10):
        print(symbol, end="", flush=True)
        time.sleep(seconds / 10)
    print(" Done!")
