# Hacking Version 4
from uagame import Window
from time import sleep

window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')
line_depth = 0

headerlist = ['DEBUG MODE', '1 ATTEMPT(S) LEFT', '']

for phrase in headerlist:
    window.draw_string(phrase, 0, line_depth)
    window.update()
    line_depth += window.get_font_height()
    sleep(0.3)

passwordlist = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']

for phrase in passwordlist:
    window.draw_string(phrase, 0, line_depth)
    window.update()
    line_depth += window.get_font_height()
    sleep(0.3)

guess = window.input_string('ENTER PASSWORD >', 0, line_depth)

if guess == 'HUNTING':
    
    correctphraselist = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
    
    window.clear()
    line_depth = (window.get_height()-7*window.get_font_height())//2
    
    for phrase in correctphraselist:
        
        window.draw_string(phrase, (window.get_width()-window.get_string_width(phrase))//2, line_depth)
        line_depth += window.get_font_height()
        window.update()
        sleep(0.3)
    
    window.input_string('PRESS ENTER TO CONTINUE', (window.get_width()-window.get_string_width('PRESS ENTER TO CONTINUE'))//2, line_depth)
 
else:

    incorrectphraselist = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
    
    window.clear()
    line_depth = (window.get_height()-7*window.get_font_height())//2

    for phrase in incorrectphraselist:
            
            window.draw_string(phrase, (window.get_width()-window.get_string_width(phrase))//2, line_depth)
            line_depth += window.get_font_height()
            window.update()
            sleep(0.3)    

    window.input_string('PRESS ENTER TO EXIT', (window.get_width()-window.get_string_width('PRESS ENTER TO EXIT'))//2, line_depth)
    
window.close()