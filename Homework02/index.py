import simplegui
import random
import math

secret_number = 0
right_border = 0
attempts_left = 0

def new_game():
    global secret_number
    global right_border
    global attempts_left    
    attempts_left = int(math.ceil(math.log((right_border + 2), 2)))
    secret_number = random.randint(0, right_border)    
    print('\nNew game. Range is [0,' + str(right_border + 1) + ')')
    print('Number of remaining guesses is ' + str(attempts_left))
    
def range_100_button_on_click():
    global right_border
    right_border = 99
    new_game()
    
def range_1000_button_on_click():
    global right_border
    right_border = 999
    new_game()

def input_guess(guess):
    global secret_number
    global attempts_left
    players_number = int(guess)
    print('\nGuess was ' + str(players_number))
    attempts_left -= 1
    print('Number of remaining guesses is ' + str(attempts_left))
    if secret_number > players_number:
        print('Higher')
    elif secret_number < players_number:
        print('Lower')
    else:
        print('Correct')
        new_game()
        pass
    
    if attempts_left == 0:
        new_game()

frame = simplegui.create_frame("Homework02", 200, 200)
frame.add_button("Rangeis[0,100)", range_100_button_on_click, 150)
frame.add_button("Rangeis[0,1000)", range_1000_button_on_click, 150)
frame.add_input("Enter", input_guess, 150)

range_100_button_on_click()