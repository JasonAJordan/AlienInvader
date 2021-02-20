import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien

#from ryan import Ryan
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf
from button import Button

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play Button.
    play_button = Button(ai_settings, screen, "Play")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    #Make a ship
    ship =Ship(ai_settings, screen)
    
    #Make a group to store bullets, and group of aliens.
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    
    #Make something fun
    #ryan = Ryan(screen,ai_settings)
    #ryan2 = Ryan(screen,ai_settings)
    #If you are actually reading this code please note that this was actually my first 
    #ever project and I wanted to add some extra stuff. 
    
    
    
    # Start the main loop for the game.
    while True:
    
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, ryan, ryan2)
        
run_game()
