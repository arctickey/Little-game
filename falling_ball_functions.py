import pygame
import sys
from ship import Ship
from ball import Ball
from pygame.sprite import Sprite


def update_screen(balls,screen,setting,ship):
    screen.fill(setting.bg_color)
    balls.draw(screen)
    ship.blitme()
    pygame.display.flip()


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup(event,ship)


def check_keydown(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True


def check_keyup(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False

def create_ball(setting,screen,balls):
    for ball_number in range(1):
        ball = Ball(screen,setting)
        balls.add(ball)


def update_balls(setting,screen,balls):
    balls.update(screen,setting)


def check_collisions(setting,screen, ship,balls):
    if pygame.sprite.spritecollideany(ship,balls):
        balls.empty()
        create_ball(setting,screen,balls)





