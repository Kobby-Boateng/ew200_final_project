import pygame
import math
from shooter import Shooter

enemies = pygame.sprite.Group()

class Enemy(pygame.sprite.Sprite):
    def __init__ (self, x,y):
        super().__init__()
        self.image = pygame.image.load("assets/fighter.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())


    def enemy_AI(self, shooter):
        enemy_x = self.rect.centerx
        enemy_y = self.rect.centery
        shooter_x = shooter.rect.centerx
        shooter_y = shooter.rect.centery

        # calculate direction vector
        total_x = shooter_x - enemy_x
        total_y = shooter_y - enemy_y

        #calculates the angle between the player and enemy
        angle_of_player = math.atan2(total_y,total_x)

        enemy_x_speed = 3*math.cos(angle_of_player)
        enemy_y_speed = 3*math.sin(angle_of_player)

        self.rect.centerx+= enemy_x_speed
        self.rect.centery+= enemy_y_speed




    def draw(self, screen):
        screen.blit(self.image, self.rect)


enemy = pygame.sprite.Group()