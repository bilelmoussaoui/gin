import fire

from gin.app import Gin

def main():
    # Required to use console_entry from setup.py
    fire.Fire(Gin)
