# Hacking Version 4
from uagame import Window
from time import sleep

def main():
    window = create_window()
    location = [0, 0]
    attempts = 4
    password = 'HUNTING'
    display_header(window, location, attempts)    
    display_password_list(window, location)
    get_guesses(window, password, location, attempts_left):

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

def display_password_list(window, location):
    passwordlist = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
    for string in passwordlist:
        display_line(window, string, location)     
    
def get_guesses(window, password, location, attempts_left):

#end_game(window, guess, password):

def display_line(window, string, location):
    window.draw_string(string, location[0], location[1])
    location[1] += window.get_font_height()    
    window.update()
    sleep(0.3)    
    
#def prompt_user(window, prompt, location):
    
#def check_warning(window, attempts_left):
    
#def display_outcome(window, outcome):


'''for phrase in passwordlist:
    window.draw_string(phrase, 0, line_depth)
    window.update()
    line_depth += window.get_font_height()
    sleep(0.3)

guess = window.input_string('ENTER PASSWORD >', 0, line_depth)
line_depth += window.get_font_height()
attemptsleft -= 1
window.draw_string(str(attemptsleft), 0, window.get_font_height())
window.update()

while attemptsleft > 0 and guess != 'HUNTING':
    window.draw_string(str(attemptsleft), 0,window.get_font_height())
    window.update()
    guess = window.input_string('ENTER PASSWORD >', 0, line_depth)
    line_depth += window.get_font_height()
    attemptsleft -= 1
    if attemptsleft == 1:
        window.draw_string('*** LOCKOUT WARNING ***', window.get_width()-window.get_string_width('*** LOCKOUT WARNING ***'),window.get_height()-window.get_font_height())
    
window.clear()
line_depth = (window.get_height()-7*window.get_font_height())//2    
    
if guess == 'HUNTING':
    
    correctphraselist = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
    
    for phrase in correctphraselist:
        
        window.draw_string(phrase, (window.get_width()-window.get_string_width(phrase))//2, line_depth)
        line_depth += window.get_font_height()
        window.update()
        sleep(0.3)
    
    window.input_string('PRESS ENTER TO CONTINUE', (window.get_width()-window.get_string_width('PRESS ENTER TO CONTINUE'))//2, line_depth)
 
else:

    incorrectphraselist = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']

    for phrase in incorrectphraselist:
            
        window.draw_string(phrase, (window.get_width()-window.get_string_width(phrase))//2, line_depth)
        line_depth += window.get_font_height()
        window.update()
        sleep(0.3)    

    window.input_string('PRESS ENTER TO EXIT', (window.get_width()-window.get_string_width('PRESS ENTER TO EXIT'))//2, line_depth)
    
window.close() '''

main()