import random
from words import words

# To choose a valid word from the list
def valid_word():
    word = random.choice(words)
    while('-' in word or '' in word):
        word = random.choice(words)
        
    return word.lower()

# main code
def hangman():
    guess_word = valid_word()
    print(f'hint :- {guess_word}')
    print('Computer has choosed a word, start guessing the characters')
    
    while(1):
        user_input = input('Choose a character !!')
        if(user_input in guess_word):
            print('Good Guess')
            guess_word.remove(user_input)
            if(len(guess_word) == 0):
                print('Congratulations, you guessed the word correctly')
                return
        else:
            print('OOPS, wrong guess try again')
            continue
            
hangman()