import pygame
#from settings import *

class Shooter:
    def __init__(self ,x,y):
        self.image = pygame.image.load("assets/fighter.png")
        shooter_image = self.image
        self.image = pygame.transform.scale(shooter_image, (75, 75))
        # creating a rectangle that defines where to paint fighter
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
        if self.moving_right:
            self.rect.x += 2
        if self.moving_up:
            self.rect.y -= 2
        if self.moving_down:
            self.rect.y += 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)