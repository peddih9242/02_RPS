rps_list = ["rock", "paper", "scissors"]
comp_index = 1

for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options
        result = "Loss"
        if user_choice == comp_choice:
            result = "Tie"
        elif user_choice == "paper" and comp_choice == "rock":
            result = "Win"
        elif user_choice == "rock" and comp_choice == "scissors":
            result = "Win"
        elif user_choice == "scissors" and comp_choice == "paper":
            result = "Win"

        print("You chose {}, the computer chose {}. Result: {}".format(user_choice, comp_choice, result))
