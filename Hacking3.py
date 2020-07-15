# Hacking Version 3
from uagame import Window
from time import sleep

window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

line_depth = 0

window.draw_string('DEBUG MODE', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('1 ATTEMPT(S) LEFT', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('PROVIDE', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('SETTING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('CANTINA', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('CUTTING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('HUNTERS', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('SURVIVE', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('HEARING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('HUNTING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('REALIZE', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('NOTHING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('OVERLAP', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('FINDING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('PUTTING', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

window.draw_string('', 0, line_depth)
window.update()
line_depth += window.get_font_height()
sleep(0.3)

guess = window.input_string('ENTER PASSWORD >', 0, line_depth)

if guess == 'HUNTING':

    window.clear()
    line_depth = (window.get_height()-7*window.get_font_height())//2

    window.draw_string(guess, (window.get_width()-window.get_string_width(guess))//2, line_depth)
    line_depth += window.get_font_height()
    window.update()
    sleep(0.3)

    window.draw_string('', 0, line_depth)
    line_depth += window.get_font_height()
    window.update()
    sleep(0.3)

    window.draw_string('EXITING DEBUG MODE', (window.get_width()-window.get_string_width('EXITING DEBUG MODE'))//2, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.draw_string('', 0, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.draw_string('LOGIN SUCCESSFUL - WELCOME BACK', (window.get_width()-window.get_string_width('LOGIN SUCCESSFUL - WELCOME BACK'))//2, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.draw_string('', 0, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.input_string('PRESS ENTER TO CONTINUE', (window.get_width()-window.get_string_width('PRESS ENTER TO CONTINUE'))//2, line_depth)

    window.close()    
    
else:

    window.clear()
    line_depth = (window.get_height()-7*window.get_font_height())//2

    window.draw_string(guess, (window.get_width()-window.get_string_width(guess))//2, line_depth)
    line_depth += window.get_font_height()
    window.update()
    sleep(0.3)

    window.draw_string('', 0, line_depth)
    line_depth += window.get_font_height()
    window.update()
    sleep(0.3)

    window.draw_string('LOGIN FAILURE - TERMINAL LOCKED', (window.get_width()-window.get_string_width('LOGIN FAILURE - TERMINAL LOCKED'))//2, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.draw_string('', 0, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.draw_string('PLEASE CONTACT AN ADMINISTRATOR', (window.get_width()-window.get_string_width('PLEASE CONTACT AN ADMINISTRATOR'))//2, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.draw_string('', 0, line_depth)
    window.update()
    sleep(0.3)
    line_depth += window.get_font_height()

    window.input_string('PRESS ENTER TO EXIT', (window.get_width()-window.get_string_width('PRESS ENTER TO EXIT'))//2, line_depth)

    window.close()