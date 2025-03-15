import pygame
import sys

pygame.init()


# Creation of main variables, which can be referenced during all stages of the creation of the game
HEIGHT = 800
WIDTH = 600
timer = pygame.time.Clock()
fps = 60


screen = pygame.display.set_mode((800,600))
# creation of the screen window that the user will see when they open the game
pygame.display.set_caption("Metamaze")
# this changes the game name from pygame window to Metamaze, which is the name of the

while True:
    timer.tick(fps)
    screen.fill("purple")



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # when exit is called, the while True loop is clsoed
    #  draw all of our elements
    # update all our elements, shown by set_mode
    pygame.display.update()
    # anything drawn is displayed to the player



