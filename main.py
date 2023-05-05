import os
from dotenv import load_dotenv, find_dotenv

from src.print_header import print_header
from src.ia import ia

def launch_ai(api_key):
    print_header()
    ia(api_key)


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    api_key = os.environ.get("KEY")
    launch_ai(api_key)
