#!/usr/bin/env python

"""
main.py:
    main function of the project
"""

from src.print_header import print_header
from src.ia import ia

from src.data import Data
from src.init_data import init_data
from src.pre_prompt import pre_prompt

def launch_ai(data: Data):
    print_header()
    pre_prompt(data.log_file)
    ia(data)


if __name__ == "__main__":
    data = init_data()
    launch_ai(data)
