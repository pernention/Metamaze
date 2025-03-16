import pygame


Height = 400


class Menu:
    def __init__(self): # Initializing pygame
        self.Title = pygame.font.SysFont("Calibri", 30)

        
        # Render buttons text
        self.start = self.Title.render("Start", True, (25,25,25))
        self.settings = self.Title.render("Settings", True, (25,25,25))
        self.opt = self.Title.render("Option", True, (25,25,25))

        self.start_rect = pygame.Rect(10, Height-150, 10, 10)
        self.settings_rect = pygame.Rect(10, Height-100, 10, 10)
        self.opt_rect = pygame.Rect(10, Height-50, 10, 10)
        



    def draw(self, win):

        # Draw Start button
        win.blit(self.start, (self.start_rect.x, self.start_rect.y))
        # Draw Settings button
        win.blit(self.settings, (self.settings_rect.x, self.settings_rect.y))
        # Draw Options button
        win.blit(self.opt, (self.opt_rect.x, self.opt_rect.y))