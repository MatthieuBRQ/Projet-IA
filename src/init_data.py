#!/usr/bin/env python

"""
init_data.py:
    initiate a Data object
"""

import os, openai
from dotenv import load_dotenv, find_dotenv

from src.data import Data


def get_key():
    load_dotenv(find_dotenv())
    return os.environ.get("KEY")


def init_data() -> Data:
    data = Data()

    data.api_key = get_key()
    openai.api_key = data.api_key
    return data
