import pygame

pygame.init()


# Creating button class

font = pygame.font.SysFont("arialblack", 50)

class Button ():
    def __init__(self, x_position, y_position, text, width = 200, height = 50):

        # Creating methods
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.text = text
        self.text = font.render(self.text, True, "White")
        self.text.rect = self.text.get_rect(center=(self.x_position,self.y_position))
        
    def draw(self, screen):
        # Draw blue rectangle button
        pygame.draw.rect(screen, (0,128,255), self.rect) 


    def button_clicked(self, mouse_position):
        # Checks if button is clicked
        return self.rect.collidepoint(mouse_position)
    