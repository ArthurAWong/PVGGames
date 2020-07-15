from uagame import Window
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from random import randint 

def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()
    
def create_window():
    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')   
    return window    

def create_game(window):
    game = Game()
    game.window = window
    game.close_selected = False
    small_radius = 30
    small_center = generate_center(game, small_radius)
    game.small_dot = create_dot('red', small_radius, small_center, [1, 2])
    big_radius = 40
    big_center = generate_center(game, big_radius)
    game.big_dot = create_dot('blue', 40, big_center, [2, 1])
    game.clock = Clock()
    game.window.set_font_name('ariel')
    game.window.set_font_color('white')
    game.window.set_font_size(40)    
    return game

def generate_center(game, radius):
    center = [0, 0]
    center[0] = randint(radius, game.window.get_width() - radius)
    center[1] = randint(radius, game.window.get_height() - radius)
    
    return center

def create_dot(color, radius, center, velocity):
    dot = Dot()
    dot.color = color
    dot.radius = radius
    dot.center = center
    dot.velocity = velocity
    return dot

def play_game(game):
    while not game.close_selected:
        handle_events(game)
        draw_game(game)
        update_game(game)
        
def handle_events(game):
    event_list = get_events()
    for event in event_list:
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            game.small_dot.center = generate_center(game, game.small_dot.radius)
            game.big_dot.center = generate_center(game, game.big_dot.radius)
    
def draw_game(game):
    game.window.clear()
    draw_score(game) 
    draw_dot(game, game.big_dot)
    draw_dot(game, game.small_dot)  
    game.window.update()

def draw_score(game):
    game.score = get_ticks() // 1000
    game.window.draw_string('Score: ' + str(game.score), 0, 0)     

def draw_dot(game, dot):
    surface = game.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)
        
def update_game(game):
    frame_rate = 90    
    move_dot(game, game.big_dot)
    move_dot(game, game.small_dot)    
    game.clock.tick(frame_rate)

def move_dot(game, dot):
    size = [game.window.get_width(), game.window.get_height()]
    for index in range(0,2):
        dot.center[index] = dot.center[index] + dot.velocity[index]
        if dot.center[index] + dot.radius >= size[index] or dot.center[index] - dot.radius <= 0:
            dot.velocity[index] = - dot.velocity[index]

class Game:
    
    pass

class Dot:
    
    pass

main()