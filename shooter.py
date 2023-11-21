import pygame
#from settings import *

class Shooter(pygame.sprite.Sprite):
    def __init__(self ,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/fighter.png")
        shooter_image = self.image
        self.image = pygame.transform.scale(shooter_image, (75, 75))
        # creating a rectangle that defines where to paint fighter
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.health = 100

    def draw(self):
        pygame.draw.circle( self.color, (self.x, self.y), self.radius)

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
        if self.moving_right:
            self.rect.x += 2
        if self.moving_up:
            self.rect.y -= 2
        if self.moving_down:
            self.rect.y += 2

    #def player_health (self, health):
        #self.health = 40

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class bullet(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing