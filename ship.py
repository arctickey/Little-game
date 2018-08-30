import settings
import pygame



class Ship:
    def __init__(self, screen,setting):
        self.screen = screen
        self.setting = setting
        self.image = pygame.image.load("C:/Users/Filip/Desktop/Projekty/Alien_Invasion/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.move_right = False
        self.move_left = False

    def update(self,screen, setting):
        if self.move_right:
            self.rect.centerx += setting.speed_ship_factor
        if self.move_left:
            self.rect.centerx -= setting.speed_ship_factor
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += setting.speed_ship_factor
        if self.move_left and self.rect.left > 0:
            self.center -= setting.speed_ship_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)



