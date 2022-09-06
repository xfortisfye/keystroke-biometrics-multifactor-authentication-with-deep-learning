"""
combi
"""
import os
import platform
import time
from sys import exit

# keyboard
from pynput.keyboard import Key, Listener
from keyboard import Keyboard
import csv
from time import sleep
import random

def main():
    startFlag = True

    while startFlag is True:
        print("What kind of dataset will you like to generate? \n"
        + "1) Exp 1: Random 10-Letters Dataset for CAPTCHA\n"
        + "2) Exp 2: Identical 10-Letters Dataset for CAPTCHA\n"
        + "3) Exp 3: Controlled dataset for Password\n"
        + "4) Exp 3: Controlled dataset for Password\n"
        + "5) Exp 4: \n"
        + "6) Exp 4: \n"
        + "7) Exp 4: ")
        case = input()
        case = int(case)
        print(case)
        if case == 1:
            print('two')

        elif case == 5:
            print('five')

        elif case == 7:
            print('seven')

        else:
            print("Please select the appropriate case number.")

if __name__ == "__main__":
    main()

    # generate ui file
    # pyuic5 mainwindow.ui -o mainwindowui.py
    # generate resource file
    # pyrcc5 resources.qrc -o resources.py
    # create app
    # pyinstaller -F -w main.py
    # pyinstaller --onefile main.py
    # pyinstaller main.py --onefile --hidden-import=pynput.keyboard._xorg -n combi
