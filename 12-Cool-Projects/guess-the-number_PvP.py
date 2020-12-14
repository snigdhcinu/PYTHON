import random

def start():
    answer = input('Player-1 Enter a Number : ')
    guess = input('Player-2 Guess the number : ')
    
    while(1):
        if(guess == answer):
            print('✔ Awesome, Your guess was correct !! 🔥🔥🔥🔥')
            return
        else:
            if(guess > answer):
                print(' 👎 Try again with a smaller number ')
                break
            else:
                print('👎 Try again with a bigger number')
                break
                    

start()