import random

def dice_roller1(pos):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    flag = 0
    print(f"P1 dice roll is {dice1},{dice2}")
    dice = dice1+dice2
    pos = pos+dice
    if pos%10 == 0 and 1<pos<100:
        print("Oops! You have encountered a snake.")
        if pos ==10:
            pos = pos-9
        else:
            pos= pos - 10
    else:
        if pos == 100:
            print("P1 has won!")
            flag = 1
        if pos > 100:
            print("Invalid position, try again")
            pos = pos-dice
        if pos == 99:
            print("You cant win now, better luck next time")
            flag = 2
    return flag,pos

def dice_roller2(pos):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    flag = 0
    print(f"P2 dice roll is {dice1},{dice2}")
    dice = dice1+dice2
    pos = pos+dice
    if pos%10 == 0 and 1<pos<100:
        print("Oops! You have encountered a snake.")
        if pos ==10:
            pos = pos-9
        else:
            pos= pos - 10
    else:
        if pos == 100:
            print("P2 has won!")
            flag = 1
        if pos > 100:
            print("Invalid position, try again")
            pos = pos-dice
        if pos == 99:
            print("You cant win now, better luck next time")
            flag = 2
    return flag,pos



def main():
    print("Welcome to the snake and ladder game, the rules are simple, there are 1 to 100 blocks, at every 10th block there is a snake which takes you back 10 places. You have two dices to roll.")
    roll = 't'
    pos1 = 1
    pos2 = 1
    while roll == 't':
        flag1,pos1 = dice_roller1(pos1)
        flag2,pos2 = dice_roller2(pos2)
        if flag1 == 1 or flag2 == 1:
            break
        if flag1 == 2:
            print("Player 2 has won by default")
        if flag2 == 2:
            print("Player 1 has won by default")
        print(f"P1 position is {pos1}")
        print(f"P2 position is {pos2}")
        roll = input("Enter t to roll again")


main()