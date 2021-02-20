import pygame
from random import randint

class Ryan():

    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        
        # Load the ryan image and get its rect.
        self.image = pygame.image.load('images/ryan.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #randomizer 
        random_number_x = randint(0 + self.rect.width, ai_settings.screen_width - self.rect.width)
        random_number_y = randint(0 + self.rect.height, ai_settings.screen_height - self.rect.height)
        
        # Start each new ryan at the center of the screen.
        self.rect.centerx = random_number_x
        self.rect.centery = random_number_y
        
    def blitme(self):
        """Draw the ryan at its current location."""
        self.screen.blit(self.image, self.rect)
        




"""        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        """
