import random
# roll the dice game

# not updatable variables
player_points = 0
bot_points = 0

laps = 0

while True:
    if (player_points < 3) and (bot_points < 3):
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

    elif (player_points >= 3) or (bot_points >= 3):
        if player_points >= bot_points:
            print("You won the game.")
            q = input("enter... ")
            break
        elif player_points < bot_points:
            print("You lose the game.")
            q = input("enter... ")
            break