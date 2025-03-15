import pygame
import sys

pygame.init()


# Creation of main variables, which can be referenced during all stages of the creation of the game
HEIGHT = 800
WIDTH = 600
timer = pygame.time.Clock()
fps = 60

game_paused = False


screen = pygame.display.set_mode((800,600))
# creation of the screen window that the user will see when they open the game
pygame.display.set_caption("Metamaze")
# this changes the game name from pygame window to Metamaze, which is the name of the

# creation of font, as well as text colour
font = pygame.font.SysFont("arialblack", 25)
text_color = (255, 0, 255)



def draw_buttons(text, font, text_color, x, y)
run = True
while True:


    
    class Menu:
    
        def __init__(self, ):
            self.stuff = passed_stuff_however_necessary
        

        def event(self, event):
            # checks for events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return None  
            # when the event key is pressed, nothing happens
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_paused = True
               

                # when the spacebar key is pressed, the game is paused



            while True:
                timer.tick(fps)
                screen.fill("purple")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    else:
                        if state.event(event) is None:
                            exit()





