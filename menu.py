import pygame
import sys
import button

pygame.init()


# Variables
HEIGHT = 800
WIDTH = 600
timer = pygame.time.Clock()
fps = 60




screen = pygame.display.set_mode((800,600))
# Main Screen
pygame.display.set_caption("Metamaze")


class Menu:
    ...
class Game:
    ...



game_state = "Main Menu"
menu = Menu()
game = Game()

# Allows Exit game
while True:
    timer.tick(fps)
    screen.fill("purple")

    if game_state == "Main menu":
        state = menu
    elif game_state == "game":
        state = game  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
            # While true loop is closed
        else:
            if state.event(event) is None:
                exit()

    state.update()
    state.draw(screen)


    pygame.display.update()








