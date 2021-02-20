import sys
import pygame

def make_ryans(ai_settings, screen, ryan):
    ryan = Ryan(ai_settings, screen)
    




def create_star(ai_settings, screen, stars, star_number):
    """Create star and place it in its location in the row."""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height
    
    available_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = available_space_x // (2 * star_width)
    
    available_space_y = ai_settings.screen_height - 2 * star_height
    number_rows_y = available_space_y // (2 * star_height)
    
    
    random_number = randint(0, number_rows_y)
    #This programer made a random number from 0 - available pixels space 
    
    star.x = star_width + 2 * star_width * star_number
    #star.y = star_height + 2 * star_height * row_number
    star.y = star_height + 2 * star_height * random_number
    star.rect.x = star.x
    star.rect.y = star.y
    
    stars.add(star)
    #how does this work. when did it appear.
