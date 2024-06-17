import random

def number_guess():
    num = random.randint(0,100)
    count = 0
    choice = 'n'
    guess = input("I am thinking of a number in range 0 to 100, can you guess it?")
    guess = int(guess)
    for i in range(0,3):
        if guess == num:
            print("Congratulations, you won!")
            choice = input("Would you like to play again? Type y if yes, n if no.")
            break
        else:
            if count == 0:
                print("Thats not right, here is a hint to help you find the number")
                high_or_low(num,guess)
                guess = input("Try again you have 3 chances")
                guess = int(guess)
                count+=1
            elif count == 1:
                print("Thats not right, here is a hint to help you find the number")
                divisible(num)
                guess = input("Try again, you have 2 chances")
                guess = int(guess)
                count+= 1
            else:
                print("Thats not right, here is a hint to help you find the number")
                prime(num)
                guess = input("Try again, you have 1 chances")
                guess = int(guess)
                count+=1
    count = 0
    choice = input(f"You have run out of chances, the number is {num} would you like to play again, type y if yes, n if no")
    return choice
    

def high_or_low(num,guess):
    if num > guess:
        print("You need to look higher.")
    else:
        print("You need to look lower.")

def divisible(num):
    if num%3 == 0 and num%5 == 0:
        print("The number is divisible by both 3 and 5") 
    elif num%3 == 0:
        print("The number is divisible by 3")
    elif num%5 == 0:
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 3 or 5")

def prime(num):
    f=0
    for i in range(2,num):
        if num%i == 0:
            f=f+1
    if f==0:
        print("The number is prime number")
    else:
        print("The number is not a prime number")

def main():
    choice = 'y'
    while choice == 'y':
        choice = number_guess()
    if choice == 'n':
        print("Thanks for playing")

main()