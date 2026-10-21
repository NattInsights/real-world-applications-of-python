import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100 inclusive:"))
if guess > 100 or guess < 1:
    print("Number out of range")
if guess > number:
    print("Higher!")
    guess = int(input("Try again:"))
elif guess < number:
    print("Lower!")
    guess = int(input("Try again:"))
elif guess == number:
    print("You guessed correctly!")