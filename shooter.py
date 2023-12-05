import pygame
#from settings import *


bullets = pygame.sprite.Group()
missiles = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()

class Shooter(pygame.sprite.Sprite):
    def __init__(self ,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/brawler.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.right_image = pygame.transform.flip(self.image,False, False)
        self.left_image = pygame.transform.flip(self.image, True, False)
        self.up_image = pygame.transform.rotate(self.image, 90)
        self.down_image = pygame.transform.rotate(self.image, 270)
        self.up_right_image = pygame.transform.rotate(self.image, 45)
        self.down_right_image = pygame.transform.rotate(self.image, 315)
        self.down_left_image = pygame.transform.rotate(self.image, 225)
        self.up_left_image = pygame.transform.rotate(self.image, 135)
        self.rect = self.image.get_rect()
        self.loser_image = pygame.image.load("assets/loser.png")
        self.loser_image = pygame.transform.scale(self.loser_image, (100,100))
        # creating a rectangle that defines where to paint fighter
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.health = 100

    def draw(self):
        pygame.draw.circle( self.color, (self.x, self.y))

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 2
            self.image = self.left_image
        if self.moving_right and self.rect.right < 1300 :
            self.rect.x += 2
            self.image = self.right_image
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
            self.image = self.up_image
        if self.moving_down and self.rect.bottom < 600:
            self.rect.y += 2
            self.image = self.down_image
        if self.moving_right and self.moving_up:
            self.image = self.up_right_image
        if self.moving_right and self.moving_down:
            self.image = self.down_right_image
        if self.moving_up and self.moving_left:
            self.image = self.up_left_image
        if self.moving_down and self.moving_left:
            self.image = self.down_left_image
        if self.health <= 7:
            self.image = self.loser_image

    #def player_health (self, health):
        #self.health = 40

    def draw(self, screen):
        screen.blit(self.image, self.rect)



