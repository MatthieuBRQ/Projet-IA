#!/usr/bin/env python

"""
init_data.py:
    initiate a Data object
"""

import os
from dotenv import load_dotenv, find_dotenv

from data import Data


def get_key():
    load_dotenv(find_dotenv())
    return os.environ.get("KEY")


def init_data() -> Data:
    data = Data()

    data.api_key = get_key()
    return data
