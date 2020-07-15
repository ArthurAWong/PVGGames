from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():
    window = create_window()
    clock = Clock()
    
    big_color = 'blue'
    big_radius = 40
    big_center  = [200, 100]
    big_velocity = [2, 1]
    
    small_color = 'red'
    small_radius = 30
    small_center = [50, 75]
    small_velocity = [1, 2]
    
    play_game(window, big_color, big_center, big_radius, big_velocity, small_color, small_radius, small_center, small_velocity, clock)
    window.close()
    
def create_window():
    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')   
    return window    

def play_game(window, big_color, big_center, big_radius, big_velocity, small_color, small_radius, small_center, small_velocity, clock):
    close_selected = False
    while not close_selected:
        close_selected = handle_events()
        draw_game(window, big_color, big_center, big_radius, small_color, small_radius, small_center)
        update_game(window, big_center, big_radius, big_velocity, small_radius, small_center, small_velocity, clock)
        
def handle_events():
    closed = False
    event_list = get_events()
    for event in event_list:
        if event.type == QUIT:
            closed = True
    return closed
    
def draw_game(window, big_color, big_center, big_radius, small_color, small_radius, small_center):
    window.clear()
    draw_dot(window, big_color, big_center, big_radius)
    draw_dot(window, small_color, small_center, small_radius)
    window.update()
    
def draw_dot(window, color_string, center, radius):
    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)
        
def update_game(window, big_center, big_radius, big_velocity, small_radius, small_center, small_velocity, clock):
    frame_rate = 90
    move_dot(window, big_center, big_radius, big_velocity)
    move_dot(window, small_center, small_radius, small_velocity)
    clock.tick(frame_rate)

def move_dot(window, center, radius, velocity):
    size = [window.get_width(), window.get_height()]
    for index in range(0,2):
        center[index] = center[index] + velocity[index]
        if center[index] + radius >= size[index] or center[index] - radius <= 0:
            velocity[index] = - velocity[index]
    
main()