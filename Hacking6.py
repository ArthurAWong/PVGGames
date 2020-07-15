# Hacking Version 6
from uagame import Window
from time import sleep
from random import randint, choice

def main():
    window = create_window()
    location = [0, 0]
    attempts = 4
    size = 20
    password = 'HUNTING'
    display_header(window, location, attempts)    
    display_password_list(window, location, size)
    attempts_left = attempts
    guess = get_guesses(window, password, location, attempts_left)
    outcome = [end_game(window, guess, password), guess]
    display_outcome(window, outcome)

def create_window():
    window = Window('Hacking', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')   
    return window

def display_header(window, location, attempts):
    headerlist = ['DEBUG MODE', str(attempts) + ' ATTEMPT(S) LEFT', '']
    for string in headerlist:
        display_line(window, string, location)    

def display_password_list(window, location, size):
    passwordlist = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING']
    for string in passwordlist:
        embedded_password = embed_password(string, size)
        display_line(window, embedded_password, location)  
    display_line(window, '', location)
    
def get_guesses(window, password, location, attempts_left):
    prompt = 'ENTER PASSWORD >'
    guess_location = [window.get_width() // 2, 0]
    while True:
        guess = prompt_user(window, prompt, location)
        attempts_left -= 1
        if guess == password or attempts_left == 0:
            return guess        
        window.draw_string(str(attempts_left), 0, window.get_font_height())
        check_warning(window, attempts_left)
        display_hint(window, password, guess, guess_location)
        
def end_game(window, guess, password):
    if guess == password:
        return True
    else:
        return False

def display_line(window, string, location):
    window.draw_string(string, location[0], location[1])
    location[1] += window.get_font_height()    
    window.update()  
    sleep(0.3)
    
def prompt_user(window, prompt, location):
    entry = window.input_string(prompt, location[0], location[1])
    location[1] += window.get_font_height()    
    return entry
    
def check_warning(window, attempts_left):
    if attempts_left == 1:
        window.draw_string('*** LOCKOUT WARNING ***', window.get_width()-window.get_string_width('*** LOCKOUT WARNING ***'),window.get_height()-window.get_font_height())
        window.update()
        
def display_outcome(window, outcome):
    window.clear()
    location = [0, (window.get_height()-7*window.get_font_height()) // 2]
    if outcome[0]:
        correctphraselist = [outcome[1], '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        for phrase in correctphraselist:
            location[0] = (window.get_width()-window.get_string_width(phrase))//2
            display_line(window, phrase, location)
            
        location[0] = (window.get_width()-window.get_string_width('PRESS ENTER TO CONTINUE')) // 2
        prompt_user(window, 'PRESS ENTER TO CONTINUE', location)
    else:
        incorrectphraselist = [outcome[1], '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
        for phrase in incorrectphraselist:
            location[0] = (window.get_width()-window.get_string_width(phrase))//2
            display_line(window, phrase, location)
        
        location[0] = (window.get_width()-window.get_string_width('PRESS ENTER TO EXIT')) // 2
        prompt_user(window, 'PRESS ENTER TO EXIT', location)  
        
def embed_password(password, size):
    fill = '!@#$%^&*()-+=~[]{}'
    embedding = ''
    password_size = len(password)
    split_index = randint(0, size - password_size)
    for index in range(0, split_index):
        embedding += choice(fill)    
    embedding += password
    for index in range(split_index + password_size, size):
        embedding += choice(fill)
    return embedding

def display_hint(window, password, guess, guess_location):
    correct_letters = 0
    if len(password) < len(guess):
        max_index = len(password)
    else:
        max_index = len(guess)
    for index in range(0, max_index):
        if guess[index] == password[index]:
            correct_letters += 1
    display_line(window, guess + ' INCORRECT', guess_location)
    display_line(window, str(correct_letters) + '/' + str(len(password)) + ' IN MATCHING POSITIONS', guess_location)

main()