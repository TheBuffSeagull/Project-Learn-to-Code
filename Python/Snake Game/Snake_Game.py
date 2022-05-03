# Example code from https://www.edureka.co/blog/snake-game-with-pygame/#install
# 5/3/22 || Learning to code so it's time for some SNAKE

import pygame

import time # getting time for a couple of extra shit I wanted
import datetime
now = datetime.datetime.now()

import random

pygame.init() # Init's all the imported pygame modules above

# Pygame uses RGB colors
# Defined as tuples as we aint gonna change default color values
blue = (0, 0, 255) 
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)



# creates display with given size (stored the numbers as vars to make it easy)
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))

game_title = 'Snake game by TheBuffSeagull' + str(now)
pygame.display.set_caption(str(game_title)) # title the window

# Here is where I keep my init cords
x1 = dis_width/2
y1 = dis_height/2



clock = pygame.time.Clock() # keep track of time via ticks

snake_speed = 30 # keeping track of speed in var for later
snake_block = 10 # how big the snake is

font_style = pygame.font.SysFont(None, 30) # creating font for message
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])


def gameLoop(): # Main Game Loop Function
    game_over = False
    game_close = False

    # Here is where I keep my init cords gaze upon them
    x1 = dis_width / 2
    y1 = dis_height / 2

    # These bad boys hold so many coordinates for me
    x1_change = 0
    y1_change = 0

    # food time
    foodx = round(random.randrange(0, dis_width - snake_block) /10) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) /10) * 10.0

    while not game_over: # while loop to read input out to us in a print statement
        
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN():
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if statement to make close button work
                game_over = True
            
            if event.type == pygame.KEYDOWN: # KEYDOWN takes inputs for movement
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                else:
                    None
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # defined border for game over if wall touched
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue,[foodx, foody, snake_block, snake_block]) # <--- snake that uses the x and y cords we are getting from keydown
        pygame.draw.rect(dis, black,[x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y == foody:
            print("Got one!")
        
        clock.tick(snake_speed) # creates a time reference per loop

    message("You lost", red) 
    pygame.display.update()
    time.sleep(2) # wait before exiting and also.... NOW I KNOW HOW TO MANIPULATE CODE TO WAIT 


    pygame.quit()
    quit()

gameLoop()