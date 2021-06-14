import random

hidden = random.randint(1,50)
#print(hidden)
guess = int(input('Guess the hidden number:'))
while guess != hidden:
    if guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess = int(input('Try another guess : '))
    
print(guess, 'was correct.')