import pygame
import math

class Enemy(pygame.sprite.Sprite):
    def __init__ (self, x,y):
        super().__init__()
        self.image = pygame.image.load("assets/enemies.png")
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def enemies_AI(self, shooter):
        enemy_x = self.rect.centerx
        enemy_y = self.rect.centery
        shooter_x = shooter.rect.centerx
        shooter_y = shooter.rect.centery

        # calculate direction vector
        total_x = shooter_x - enemy_x
        total_y = shooter_y - enemy_y

        #calculates the angle between the player and enemy
        angle_of_player = math.atan2(total_y,total_x)

        enemy_x_speed = .9*math.cos(angle_of_player)
        enemy_y_speed = .9*math.sin(angle_of_player)

        self.rect.centerx+= enemy_x_speed
        self.rect.centery+= enemy_y_speed


    def draw(self, screen):
        screen.blit(self.image, self.rect)

enemy = pygame.sprite.Group()