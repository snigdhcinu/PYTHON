import random

def start():
    answer = input('Player-1 Enter a Number : ')
    
    while(1):
        guess = input('Player-2 Guess the number : ')
        if(guess == answer):
            print('✔ Awesome, Your guess was correct !! 🔥🔥🔥🔥')
            break
        elif(guess > answer):
            print(' 👎 Try again with a smaller number ')
            continue
        else:
            print('👎 Try again with a bigger number')
            continue
                 
    return   

start()