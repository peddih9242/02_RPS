rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options
        if user_choice == "rock":
            if comp_choice == "rock":
                result = "Tie"
            elif comp_choice == "paper":
                result = "Lose"
            elif comp_choice == "scissors":
                result = "Win"
        if user_choice == "paper":
            if comp_choice == "rock":
                result = "Win"
            elif comp_choice == "paper":
                result = "Tie"
            elif comp_choice == "scissors":
                result = "Loss"
        if user_choice == "scissors":
            if comp_choice == "rock":
                result = "Loss"
            elif comp_choice == "paper":
                result = "Win"
            elif comp_choice == "scissors":
                result = "Tie"
        print("You chose {}, the computer chose {}. Result: {}".format(user_choice, comp_choice, result))