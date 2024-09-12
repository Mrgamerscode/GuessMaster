from mimetypes import guess_type
import random
import os

#guessing between 1 and 100

number = random.randint(1,100)
guess = input("guess a number between 1 and 100")
guess = int(guess)

if guess == number:
    print("wha-how, what are you, psychic?")
else:
    print("better luck next time.")
    
