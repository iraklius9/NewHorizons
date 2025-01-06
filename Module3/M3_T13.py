import time
from datetime import datetime
import os

DIGITS = {
    "0": [" ### ", "#   #", "#   #", "#   #", " ### "],
    "1": ["  #  ", " ##  ", "  #  ", "  #  ", " ### "],
    "2": [" ### ", "    #", " ### ", "#    ", "#####"],
    "3": [" ### ", "    #", " ### ", "    #", " ### "],
    "4": ["#   #", "#   #", "#####", "    #", "    #"],
    "5": ["#####", "#    ", " ### ", "    #", " ### "],
    "6": [" ### ", "#    ", "#### ", "#   #", " ### "],
    "7": ["#####", "    #", "   # ", "  #  ", "  #  "],
    "8": [" ### ", "#   #", " ### ", "#   #", " ### "],
    "9": [" ### ", "#   #", " ####", "    #", " ### "],
    ":": ["     ", "  #  ", "     ", "  #  ", "     "],
}

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    os.system('cls')

    print("CURRENT TIME")

    ascii_lines = [""] * 5
    for char in current_time:
        for i in range(5):
            ascii_lines[i] += DIGITS[char][i] + "  "

    for line in ascii_lines:
        print(line)

    time.sleep(1)
