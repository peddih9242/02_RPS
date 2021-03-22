# V2, error message included when calling function

# Functions


def choice_check(question, error):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "r" or response == "rock":
            return "rock"
        elif response == "p" or response == "paper":
            return "paper"
        elif response == "s" or response == "scissors":
            return "scissors"

        # check for exit code
        elif response == "xxx":
            return "xxx"
        else:
            print(error)

# Main routine
# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":
    # Ask for user choice and check valid
    user_choice = choice_check("Choose from rock / paper / scissors: ", "Please choose from rock / paper"
                               " / scissors (or xxx to quit)")
    # print choice for comparison
    print("You chose {}.".format(user_choice))