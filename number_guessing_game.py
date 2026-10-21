import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100 inclusive: "))

while guess != number:
    if guess > 100 or guess < 1:
        print("Number out of range")
    elif guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
  
    guess = int(input("Try again: "))

print("You guessed correctly!!")

    