import pygame
from settings import Settings
import falling_ball_functions as fbf
from ship import Ship
from pygame.sprite import Group
from ball import Ball


pygame.init()
setting = Settings()
screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
ship = Ship(screen,setting)
ball = Ball(screen,setting)
balls = Group()
fbf.create_ball(setting,screen,balls)


def run_game():
    while True:
        fbf.check_events(ship)
        ship.update(screen, setting)
        fbf.update_balls(setting,screen,balls)
        fbf.check_collisions(setting,screen,ship, balls)
        fbf.update_screen(balls, screen, setting, ship)




run_game()