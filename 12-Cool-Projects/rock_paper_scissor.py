# Rock, Paper, Scissors Game
import random as rando

choice = (('rock','paper','scissor'))

def start(choice):
    print('Write your choice from Rock, Paper, Scissor, and don"t worry about the case-sensitivity')
    while(1):
        player_choice = input('Make a choice')
        player_choice = player_choice.lower()
        print(f'Player chose : {player_choice[0].upper()}{player_choice[1:len(player_choice)]}')
        select = rando.randint(0,2)
        computer_choice = choice[select]
        print(f'Computer shows : {computer_choice}')
        
        if(computer_choice == 'rock'):
            if(player_choice == 'paper'):
                print('Congratulations, you have defeated the Computer')
                return
            elif(player_choice == 'rock'):
                print("It\'s a Draw")
                continue
            else:
                print('OOPS, you were defeated by the Computer')
                continue
            
        elif(computer_choice == 'paper'):
            if(player_choice == 'paper'):
                print('It\'s a draw ')
                continue
            elif(player_choice == 'rock'):
                print('OOPS, you were defeated by the Computer')
                continue
            else:
                print('Congratulations, you have defeated the Computer')
                return
            
        else:
            if(player_choice == 'paper'):
                print('OOPS, you were defeated by the Computer ')
                continue
            elif(player_choice == 'rock'):
                print('Congratulations, you have defeated the Computer')
                return
            else:
                print('It\'s a draw')
                continue
            
            
start(choice)
            
        