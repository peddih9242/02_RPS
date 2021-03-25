game_summary = []

rounds_played = 5
rounds_lost = 0
rounds_tied = 0

for item in range(0,5):
    result = input("Choose the result: ")
    history = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1
    elif result == "tie":
        rounds_tied += 1

    game_summary.append(history)

rounds_won = rounds_played - rounds_tied - rounds_lost

win_percent = rounds_won / rounds_played * 100
loss_percent = rounds_lost / rounds_played * 100
tie_percent = rounds_tied / rounds_played * 100

print("*** Game Summary ***")
print()
for item in game_summary:
    print(item)
print()
print("Win: {}, ({:.0f}%) \nLoss: {}, ({:.0f}%) \nTie: {}, ({:.0f}%)"
      .format(rounds_won, win_percent, rounds_lost, loss_percent, rounds_tied, tie_percent))
