import pygame
import sys
from button import Menu # Importing the "menu" class from button
# Variables

Width = 1000
Height = 400
fps = 60

pygame.init()
clock = pygame.time.Clock()


# Main Screen
win = pygame.display.set_mode((Width, Height), 0, 32)
pygame.display.set_caption("Main Menu")



# Creating game states

game_state = "menu"





def startGame():
    global state
    state = "game"

    # Resetting parameters
    # Loading states from files

def go_back_menu():
    global state
    state = "menu"


class Game:
    pass

    def draw(self, win):
        pass


def main():
    run = True

    menu  = Menu()
    game = Game()

    def draw(win):
        # Drawing objects handled here
        win.fill((144, 244, 200)) # Clears screen with background colour

        if game_state == "menu":
            menu.draw(win)
        elif game_state =="game":
            game.draw(win)

# Game states handled here

        pygame.display.update()

        # Game loop
        while run:
            print("Game loop running")
            clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "menu":
                    if menu.start_rect.collidepoint(event.pos):
                        startGame()

        draw(win)

    pygame.quit
    sys.exit()




if __name__ == "__main__":
    main()

