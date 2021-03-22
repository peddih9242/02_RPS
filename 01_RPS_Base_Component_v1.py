import random

# Functions


def choice_check(question, valid_list, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item
        # If item is not in the list, print error
        else:
            print(error)
            print()


def check_rounds():
    while True:
        response = input("How many rounds? (or press <enter> for infinite mode): ")
        round_error = "Please type either an integer that is higher than 0."
        # If infinite mode isn't chosen, check for valid response (integer that is > 0)
        if response != "":
            try:
                response = int(response)

                # If invalid response, send back to the start of the loop
                if response < 1:
                    print(round_error)
                    continue

            # If not an integer, send back to the start of the loop
            except ValueError:
                print(round_error)
                continue
        return response

# Main routine

# Lists of valid responses

yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If no, show instructions


# Ask user for # of rounds then loop

rounds_played = 0
rounds_lost = 0
rounds_tied = 0

round_amount = check_rounds()

end_game = ""
while end_game == "":
    print()
    rounds_played += 1
    if round_amount == "":
        heading = "Infinite Mode, Round {}".format(rounds_played)
    else:
        heading = "Round {} of {}".format(rounds_played, round_amount)
    print(heading)
    instruction_choose = "Please choose rock (r), paper (p) or scissors (s) or xxx to exit: "
    # get user choice and check that it's valid
    user_choice = choice_check(instruction_choose, rps_list,
                               "I don't understand, Please choose rock / paper / scissors (or xxx to quit)")
    # get computer choice
    computer_choice = random.choice(rps_list[:-1])
    if user_choice == "xxx":
        break
    if rounds_played == round_amount:
        end_game = "e"

# compare choices
    if user_choice == computer_choice:
        result = "tied"
        rounds_tied += 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "won"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "won"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1
    print("You chose {}.".format(user_choice))
    print("The computer chose {}.".format(computer_choice))
    print("You {}".format(result))

# Ask user if they want to see their game history
rounds_won = rounds_played - rounds_lost - rounds_tied

# End of game output
print()
print("***** End Game Summary *****")
print("Won: {}  |  Lost: {}  |  Tied: {}".format(rounds_won, rounds_lost, rounds_tied))

# If yes, show game history
print()
print("Thanks for playing")