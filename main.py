import pygame
#import time
from pygame.locals import *
import time

size = 40

class Frog:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("frog.jpeg").convert()
        self.image_small = pygame.transform.scale(self.image,(30,30))
        self.parent_screen = parent_screen
        self.block_x = size*3
        self.block_y = size*3

    def draw(self):
        self.parent_screen.blit(self.image_small ,
                                    (
                                    self.block_x, self.block_y))  # blit funct to draw the block on the background
        pygame.display.flip()  # the above line should be followed by this line to show the updated screen


class Snake:
    def __init__(self,surface,length):
        self.length = length # length of the snake

        self.parent_screen = surface
        self.block = pygame.image.load("block image.jpeg").convert()
        self.block_small = pygame.transform.scale(self.block, (30, 30))
        self.block_x = [size]*length
        self.block_y: int = [size]*length
        self.direction = 'down'
    def draw(self):
        self.parent_screen.fill((144, 38, 37))  # fill the background color here surface is the background the main one
        for i in range (self.length):
            self.parent_screen.blit(self.block_small,
                                (self.block_x[i], self.block_y[i]))  # blit funct to draw the block on the background
        pygame.display.flip()  # the above line should be followed by this line to show the updated screen

    def move_left(self): #move the block left
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):

        for i in range(self.length-1,0,-1): #going in the reverse direction
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
        if self.direction == 'up':
            self.block_y[0] -= size
        if self.direction == 'down':
            self.block_y[0] += size
        if self.direction == 'left':
            self.block_x[0] -= size
        if self.direction == 'right':
            self.block_x[0] += size

        self.draw()
class Game:
    def __init__(self):
        pygame.init()  # initiating pygame
        self.surface = pygame.display.set_mode((1000, 800))  # only size is given in the argument
        self.surface.fill((144, 38, 37))  # fill the background color here surface is the background the main one
        self.snake = Snake(self.surface, 6) # length -> length of the snake here 4 blocks
        self.snake.draw()
        self.frog = Frog(self.surface)
        self.frog.draw()

    def play(self): #do all the drawings if we have to call either multiple times this should be easu
        self.snake.walk()
        self.frog.draw()
    def run(self):
        running = True

        while running:  # event loop
            for event in pygame.event.get():  # event is pygame module for interacting with events and queue get->get event from queue
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_ESCAPE:  # when esc key is pressed screen is exited
                        running = False
                elif event.type == QUIT:
                    running = False
            self.play()

            time.sleep(0.3)
if __name__=="__main__":
    game = Game() #object Game
    game.run()


    pygame.display.flip() #the above line should be followed by this line to show the updated screen

 #  time.sleep(5) #after 5 sec the display will sleep /shut


