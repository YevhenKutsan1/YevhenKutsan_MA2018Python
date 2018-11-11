import random

def name_to_number(name):    
    if name.lower() == 'rock':
        return 0
    elif name.lower() == 'spock':
        return 1
    elif name.lower() == 'paper':
        return 2
    elif name.lower() == 'lizard':
        return 3
    elif name.lower() == 'scissors':
        return 4
    else:
        raise Exception('Invalid shape name')

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        raise Exception('Invalid shape number')    

def rpsls(player_choice): 
    print('\n')
    print('Player chooses ' + player_choice)
    player_number = name_to_number(player_choice)
    computer_number = random.randrange(5)
    computer_choice = number_to_name(computer_number)	
    print('Computer chooses ' + computer_choice)    
    choices_diff = (player_number - computer_number) % 5    
    if choices_diff == 0:
        print('Player and computer tie!')
    elif choices_diff < 3:
        print('Player wins!')
    else:
        print('Computer wins!')

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")