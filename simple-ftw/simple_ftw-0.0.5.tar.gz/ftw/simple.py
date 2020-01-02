#! /usr/bin/env python3
import sys
from time import sleep


def introduction(name: str):
    def reply(name: str):
        print(f"\nWelcome to the world {name.title()}! 🤗\n")

    print("Hello World!")
    sleep(1)
    print(f"Let me introduce: {name.title()}")
    sleep(2)
    reply(name)


if __name__ == '__main__':
    inputs = sys.argv[1:]
    if inputs:
        introduction(inputs[0])
    else:
        print("🙄 I require inputs!")

