# RPS computer choice v1 - Generates computer choice

import random

rps_list = ["rock", "paper", "scissors"]
for item in range(0, 21):
    computer_choice = random.choice(rps_list)
    print(computer_choice)