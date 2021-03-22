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

# Main routine

# rps list with choices
rps_list = ["rock", "paper", "scissors", "xxx"]
# loop for testing
user_choice = "xxx"
while user_choice != "xxx":

    # Ask user for choice and check that it's valid
    user_choice = choice_check("Choose from rock / paper / scissors: ", rps_list,
                               "Please enter rock / paper / scissors (or xxx to quit)")

    # Print choice for comparison purposes

    print("You chose {}".format(user_choice))