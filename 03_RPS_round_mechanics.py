# Functions
def check_rounds():
    while True:
        response = input("How many rounds: ")
        round_error = "Please type either an integer that is higher than 0."
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        return response

# Main routine

played = 0
instruction_choose = "Please choose rock (r), paper (p) or scissors (s) or xxx to exit: "

round_amount = check_rounds()
print()

end_game = ""
while end_game == "":
    played += 1
    if round_amount == "":
        heading = "Infinite Mode, Round {}".format(played)
    else:
        heading = "Round {} of {}".format(played, round_amount)
    print(heading)
    chosen = input(instruction_choose)
    print()
    if chosen == "xxx":
        break
    if played == round_amount:
        end_game = "e"
    print("You chose {}".format(chosen))
print("Thanks for playing")