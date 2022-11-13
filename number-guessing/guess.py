# A little guess the nuber game in python.
# Also used to get familiar with Git and Github

import random

print("Hello. What is you name?")
name = input()

print(f"Hi {name}, I'm thinking of a number between 1 and 20.")
secret_number = random.randint(1,20)

# Let player guess up to 6 times
for guesses in range (1, 7):
    print("Take a guess.")
    
    guess_input = input()
    guess = 0
    if guess_input.strip().isdigit():

        guess = int(guess_input)
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            # When the guess is correct.
            break
    else:
        print("Uuhhmmm... What you typed does not appear to be a number")
        print("I'm counting that as a guess though")


if guess == secret_number:
    print(f"Good job {name}! You guessed my number in {str(guesses)} guesses")
else:
    print(f"Nope. The number I was thinking of was {str(secret_number)}.")
