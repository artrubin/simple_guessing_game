from random import randint

answer = None

while answer != "n":
    guess = None
    num = None
    num = randint(1, 10)
    while guess != num:
        guess = int(input("Guess your number from 1 to 10 "))
        if guess > num:
            print("Too high")
        elif guess < num:
            print ("Too Low")
        else:
            print("You won!")
    answer = input("Would you like to play again? (y/n) ")