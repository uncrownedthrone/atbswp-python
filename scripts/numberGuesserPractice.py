import random

randomNumber = random.randint(1, 11)
print("I'm thinking of a number between 1 and 10")

for guessTaken in range(0, 10):
    print('Take a guess')
    userNumber = int(input())

    if userNumber > randomNumber:
        print('Too high. Try again.')
    elif userNumber < randomNumber:
        print('Too low. Try again.')
    else:
        break

if userNumber == randomNumber:
    print("You guessed it in " + str(guessTaken) + ' guesses!')
else:
    print("Nope. I was thinking of " + str(randomNumber))
