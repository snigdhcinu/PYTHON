import random as rnd

def start(x):
    number = rnd.randint(1,x)

    while(1):
        response = int(input(f'Guess for a number between 1 and {limit} both inclusive'))
        if(response == number):
            print(f'Voila {number} is the correct guess !!')
            return
        else:
            print('Wrong Guess Try again.')
            continue

print('Guess the game is a game where you have to guess a random number picked by computer, you have infinite chances to guess is correctly, good luck with it, happy gaming.')
input('Hit Enter key to start!')
limit = int(input('Enter Upper limit of guess'))
result = start(limit)