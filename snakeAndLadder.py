import random

def dice_roller():
    print("Welcome to the snake and ladder game, the rules are simple, there are 1 to 100 blocks, at every 10th block there is a snake which takes you back 10 places. You have two dices to roll.")
    pos = 1
    while pos in range(1,101):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"Your dice roll is {dice1},{dice2}")
        dice = dice1+dice2
        pos = pos+dice
        if pos%10 == 0 and 1<pos<100:
            print("Oops! You have encountered a snake.")
            if pos ==10:
                pos = pos-9
            else:
                pos = pos-10
        if pos == 100:
            print("You have won!")
            break
        if pos > 100:
            print("Invalid position, try again")
            pos = pos-dice
        if pos == 99:
            print("You cant win now, better luck next time")
            break
        print(f"Current position is {pos}")

dice_roller()