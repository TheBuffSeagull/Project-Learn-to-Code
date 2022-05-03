# Example code from https://www.edureka.co/blog/snake-game-with-pygame/#install
# 5/3/22 || Learning to code so it's time for some SNAKE

import pygame

pygame.init() # Init's all the imported pygame modules above


# creates display with given size you can also use (()) format for the size for some reason
dis = pygame.display.set_mode(size=(800, 600))
pygame.display.set_caption('Snake game by TheBuffSeagull') # title the window


# Pygame uses RGB colors
# Defined as tuples as we aint gonna change default color values
blue = (0, 0, 255) 
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)



game_over = False

# MAIN GAME LOOP
while not game_over: # while loop to read input out to us in a print statement
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if statement to make close button work
            game_over = True
    pygame.draw.rect(dis, white,[400, 300, 10, 10])
    pygame.display.update()
        
pygame.quit()
quit()