from random import randint

t = ["Rock","Paper","Scissors"]

computer = t[randint(0,2)]

choice = "True"

while choice == "True":
    choice = "False"
    player = input("Rock,Paper,Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose",computer,"covers",player)
        else:
            print("You win",player,"smashes",computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose",computer,"cuts",player)
        else:
            print("You win",player,"covers",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose",computer,"smashes",player)
        else:
            print("You win",player,"cuts",computer)
    else:
        print("That is not a valid input")
    choice = input("Do you want to play another game, type True if yes, False if no.")
    computer = t[randint(0,2)]