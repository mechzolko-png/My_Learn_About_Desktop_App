import random
# roll the dice game

# not updatable variables
player_points = 0
bot_points = 0

laps = 0

while True:
    # updatable variables
    bot_roll = random.randint(1, 12)
    player_roll_input = input("roll the dice: ")
    player_roll = random.randint(1, 12)

    # decision
    if bot_roll > player_roll:
        player_points -= 1
        print("your current point: ", player_points)
        print("you rolled: ", player_roll)
        print("bot rolled: ", bot_roll)
        print("You lose")
        player_decesion = input("Do you want to continue (y/n): ")
        if player_decesion == "y":
            print("Game continued")
            laps += 1
            print("laps: ", laps)
            continue
        else:
            break
    elif bot_roll <= player_roll:
        player_points += 1
        print("your current point: ", player_points)
        print("you rolled: ", player_roll)
        print("bot rolled: ", bot_roll)
        print("You won")
        player_decesion = input("Do you want to continue (y/n): ")
        if player_decesion == "y":
            print("Game continued")
            laps += 1
            print("laps: ", laps)
            continue
        else:
            break