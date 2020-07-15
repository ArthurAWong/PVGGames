from uagame import Window
from pygame import QUIT, Color, MOUSEBUTTONUP
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from random import randint 
from math import sqrt, pow

def main():
    game = Game()
    game.play_game()       

class Game:
    def __init__(self):
        self.window = Window('Poke the Dots', 500, 400)
        self._adjust_window('ariel', 'white', 64, 'black')
        self.close_selected = False
        self.collision_occured = False
        self.small_dot = Dot('red', 30, [0, 0], [1, 2], self.window)
        self.small_dot.generate_center()
        self.big_dot = Dot('blue', 40, [0, 0], [2, 1], self.window)
        self.big_dot.generate_center()
        self.clock = Clock()   
    
    def _adjust_window(self, font_name, font_color, font_size, bg_color):
        self.window.set_font_name(font_name)
        self.window.set_font_color(font_color)
        self.window.set_font_size(font_size)  
        self.window.set_bg_color(bg_color)   
    
    def handle_events(self):
        event_list = get_events()
        for event in event_list:
            if event.type == QUIT:
                self.close_selected = True
            elif event.type == MOUSEBUTTONUP:
                self.small_dot.generate_center()
                self.big_dot.generate_center()   

    def update_game(self):
        frame_rate = 90    
        self.big_dot.move_dot()
        self.small_dot.move_dot()    
        self.clock.tick(frame_rate) 
    
    def draw_score(self):
        self.score = get_ticks() // 1000
        self.window.draw_string('Score: ' + str(self.score), 0, 0)  

    def play_game(self):
        while not self.close_selected:
            self.handle_events()
            self.draw_game()
            self.update_game()
            self.collision_occured = self.big_dot.check_collision(self.small_dot)
            if self.collision_occured:
                self.end_game()
        self.window.close()
    
    def draw_game(self):
        self.window.clear()
        self.draw_score() 
        self.big_dot.draw()
        self.small_dot.draw()  
        self.window.update()   
    
    def end_game(self):
        self._adjust_window('ariel', str(self.small_dot.get_color()), 64, str(self.big_dot.get_color()))
        self.window.draw_string('GAME OVER', 0, self.window.get_height()-self.window.get_font_height())
        self.window.update() 
        while not self.close_selected:
            self.handle_events()
    
class Dot:
    def __init__(self, color, radius, center, velocity, window):
        self._color = color
        self._radius = radius
        self._center = center
        self._velocity = velocity    
        self._window = window
    
    def draw(self):
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)     
        
    def move_dot(self):
        size = [self._window.get_width(), self._window.get_height()]
        for index in range(0,2):
            self._center[index] = self._center[index] + self._velocity[index]
            if self._center[index] + self._radius >= size[index] or self._center[index] - self._radius <= 0:
                self._velocity[index] = - self._velocity[index]    
    
    def generate_center(self):
        self._center[0] = randint(self._radius, self._window.get_width() - self._radius)
        self._center[1] = randint(self._radius, self._window.get_height() - self._radius)  
        
    def get_color(self):
        return self._color
    
    def check_collision(self, dot):
        abs_delta_x = abs(self._center[0] - dot._center[0])
        abs_delta_y = abs(self._center[1] - dot._center[1])
        if sqrt(pow(abs_delta_x, 2) + pow(abs_delta_y, 2)) <= self._radius + dot._radius:
            return True

main()