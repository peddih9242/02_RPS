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
                    print()
                    continue

            # If not an integer, send back to the start of the loop
            except ValueError:
                print(round_error)
                print()
                continue
        return response


def yes_no(question):
    error = "Please answer yes or no."
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print(error)
            print()


def instructions():
    print()
    print("INSTRUCTIONS")
    print("First, choose how many rounds you want to play.")
    print("Then, make a choice of rock, paper or scissors "
          "(you can type r / p / s if you don't want to type the full word.")
    print("Paper beats rock, rock beats scissors, and scissors beats paper.")
    print()

# Main routine

# Lists of valid responses

game_summary = []
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If no, show instructions

show_instructions = yes_no("Have you played this game before? ")
if show_instructions == "no":
    instructions()

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
        rounds_played -= 1
        break
    if rounds_played == round_amount:
        end_game = "e"

# compare choices
    if user_choice == computer_choice:
        result = "TIED"
        rounds_tied += 1
    elif user_choice == "paper" and computer_choice == "rock":
        result = "WON"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "WON"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "WON"
    else:
        result = "LOST"
        rounds_lost += 1
    history = "Round {}: {}".format(rounds_played, result)
    game_summary.append(history)
    print()
    print("You chose {}.".format(user_choice))
    print("The computer chose {}.".format(computer_choice))
    print("*** You {} ***".format(result))

# Ask user if they want to see their game history
rounds_won = rounds_played - rounds_lost - rounds_tied

win_percent = rounds_won / rounds_played * 100
loss_percent = rounds_lost / rounds_played * 100
tie_percent = rounds_tied / rounds_played * 100

# End of game output
history_yesno = "yes"
if rounds_played >= 10:
    print()
    history_yesno = yes_no("Your game history has 10 rounds or over, would you like to see your results? ")
if history_yesno == "yes":
    print()
    for item in game_summary:
        print(item)
    print()
    print("***** End Game Summary *****")
    print()
    print("Win: {}, ({:.0f}%) \nLoss: {}, ({:.0f}%) \nTie: {}, ({:.0f}%)"
          .format(rounds_won, win_percent, rounds_lost, loss_percent, rounds_tied, tie_percent))

# If yes, show game history
print()
print("Thanks for playing")