import json
import time

import utils
from utils import rgb, rgb_init
from utils import Constants

print("Welcome!")
time.sleep(1)

time.sleep(1)
print(f"{Constants.PURPLE}Please select a story:")
time.sleep(1)
print(f"{Constants.CYAN}A: The Rose Mueseum")

time.sleep(1)
story = input(f"{Constants.PURPLE}Selection:{Constants.CYAN} ")
time.sleep(1)

with open("assets/stories.json", 'r') as f:
    stories = json.load(f)

if story == 'A':
    print(f"{Constants.RED}Starting The Rose Mueseum...{Constants.WHITE}\n")
    story = stories["rose-mueseum"]

time.sleep(2)

while True:
    for line in story["text"].split('\n'):
        if story["death"]:
            print(Constants.RED + line)
            
        else:
            print(Constants.PURPLE + line + Constants.WHITE)

        time.sleep(1)
            
    print("")

    if story["ending"]:
        print(f"{Constants.PURPLE}Ending: {story['ending-name']}{Constants.WHITE}")
        break

    for key, value in story["next"]["options"].items():
        print(f"{Constants.PURPLE}{key}: {Constants.CYAN}{value}")
        time.sleep(1)

    print("")

    choice = input("Choice: ")

    if not choice in story["next"]["options"]:
        print(f"{Constants.RED}That is not an option.{Constants.WHITE}\n")
        time.sleep(2)
    else:
        story = story["next"]["results"][choice]