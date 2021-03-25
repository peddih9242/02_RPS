# RPS component 6 - scoring

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

# Results

results = ["win", "win", "loss", "loss", "tie"]

for item in results:
    rounds_played += 1

    # Generate computer choice

    if item == "tie":
        rounds_tied += 1
    elif item == "loss":
        rounds_lost += 1

# calculate won
rounds_won = rounds_played - rounds_lost - rounds_tied

# print end of game statements
print()
print("***** End Game Summary *****")
print("Won: {}  |  Lost: {}  |  Tied: {}".format(rounds_won, rounds_lost, rounds_tied))