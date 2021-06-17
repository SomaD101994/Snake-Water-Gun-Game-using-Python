# Creating Snake Water Gun Game
# Import random module
import random
print('Snake - Water - Gun')

# Printing Snake, Water, Gun for Player 1
print("player1 Turn: snake, water, and gun?")

# random.randint() will randomly chose
randNo = random.randint(1, 3)

if randNo == 1:
    player1 = "snake"
elif randNo == 2:
    player1 = "water"
elif randNo == 3:
    player1 = "gun"

# Creating a function

def gameWin(player1, player2):
    # If two values are equal, declare the match is draw!
    if player1 == player2:
        return None

# Check for all possibilities when player1 chose snake

    elif player1=="snake":
        if player2 == "water":
            return False
        elif player2 == "gun":
            return True

# Check for all possibilities when player1 chose water

    elif player1=="water":
        if player2 == "snake":
            return True
        elif player2 == "gun":
            return False

# Check for all possibilities when player1 chose gun

    elif player1=="gun":
        if player2 == "snake":
            return False
        elif player2 == "water":
            return True


# Selecting the choice of Player 2

player2 = input("Your Turn: Snake, Water, or Gun?")

val = gameWin(player1, player2)

print(f"Player1 choose {player1}")

print(f"Player2 choose {player2}")

# Announce winner of every round
if val == None:
    print("The match is draw!")
elif val:
    print("You win!")
else:
    print("You lose!")