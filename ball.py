import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    def __init__(self,screen, setting):
        super().__init__()
        self.screen = screen
        self.setting = setting
        x = randint(0, setting.screen_width)
        self.image = pygame.image.load('C:/Users/Filip/Desktop/Projekty/Alien_Invasion/images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.screen_rect = screen.get_rect()
        self.y = float(self.rect.y)
        self.speed_factor = setting.object_speed_factor



    def update(self,screen,setting):
        self.y += self.setting.object_speed_factor
        self.rect.y = self.y

    def blitme(self):
        pygame.draw.rect(self.screen,self.rect)