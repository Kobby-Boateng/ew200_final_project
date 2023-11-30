import pygame
#from settings import *

bullets = pygame.sprite.Group()
missiles = pygame.sprite.Group()

class Shooter(pygame.sprite.Sprite):
    def __init__(self ,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/fighter.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.right_image = self.image
        self.left_image = pygame.transform.flip(self.image, True, False)
        self.up_image = pygame.transform.rotate(self.image, 90)
        self.down_image = pygame.transform.rotate(self.image, 270)

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
            self.image = self.left_image
        if self.moving_right:
            self.rect.x += 2
            self.image = self.right_image
        if self.moving_up:
            self.rect.y -= 2
            self.image = self.up_image
        if self.moving_down:
            self.rect.y += 2
            self.image = self.down_image

    #def player_health (self, health):
        #self.health = 40

    def draw(self, screen):
        screen.blit(self.image, self.rect)



