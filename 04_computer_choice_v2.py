# RPS computer choice v2 - Generates computer choice and ignores "xxx" in list

import random

rps_list = ["rock", "paper", "scissors", "xxx"]
for item in range(0, 21):
    computer_choice = random.choice(rps_list[:-1])
    print(computer_choice, end="\t")