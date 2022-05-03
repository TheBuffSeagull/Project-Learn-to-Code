# Example code from https://www.edureka.co/blog/snake-game-with-pygame/#install
# 5/3/22 || Learning to code so it's time for some SNAKE

import pygame
import time
import random

pygame.init() # Init's all the imported pygame modules above


# creates display with given size (stored the numbers as vars to make it easy)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by TheBuffSeagull') # title the window

snake_block = 10 # define size as var for later

# Pygame uses RGB colors
# Defined as tuples as we aint gonna change default color values
blue = (0, 0, 255) 
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Here is where I keep my init cords
x1 = dis_width/2
y1 = dis_height/2



clock = pygame.time.Clock() # keep track of time via ticks
snake_speed = 30 # keeping track of speed in var for later
snake_block = 10 # how big the snake is

font_style = pygame.font.SysFont(None, 50) # creating font for message
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False

    # These bad boys hold so many coordinates for me
    x1_change = 0
    y1_change = 0

# MAIN GAME LOOP
while not game_over: # while loop to read input out to us in a print statement
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # if statement to make close button work
            game_over = True
        
        if event.type == pygame.KEYDOWN: # KEYDOWN takes inputs for movement
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # defined border for game over if wall touched
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black,[x1, y1, 10, 10]) # <--- snake that uses the x and y cords we are getting from keydown

    pygame.display.update()

    clock.tick(snake_speed) # creates a time reference per loop

message("You lost", red) 
pygame.display.update()
time.sleep(2) # wait before exiting and also.... NOW I KNOW HOW TO MANIPULATE CODE TO WAIT 


pygame.quit()
quit()