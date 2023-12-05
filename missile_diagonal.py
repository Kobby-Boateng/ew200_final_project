import pygame

class Missile_diagonal(pygame.sprite.Sprite):
    def __init__(self, x, y, directionx, directiony):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 4
        self.image = pygame.image.load("assets/missile.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.left_image = pygame.transform.rotate(self.image,180)
        self.down_image = pygame.transform.rotate(self.image,270)
        self.up_image = pygame.transform.rotate(self.image, 90)
        self.up_right_image = pygame.transform.rotate(self.image, 45)
        self.down_right_image = pygame.transform.rotate(self.image, 315)
        self.down_left_image = pygame.transform.rotate(self.image, 225)
        self.up_left_image = pygame.transform.rotate(self.image,135)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.directionx = directionx
        self.directiony = directiony

    def update(self):
        self.rect.x += self.speed * self.directionx
        self.rect.y += self.speed * self.directiony


    def draw(self, screen):
        if self.directionx == 1 and self.directiony == 0:
            screen.blit(self.image, self.rect)
        elif self.directionx == -1 and self.directiony == 0:
            screen.blit(self.left_image, self.rect)
        elif self.directionx == 0 and self.directiony == 1:
            screen.blit(self.down_image, self.rect)
        elif self.directionx == 0 and self.directiony == -1:
            screen.blit(self.up_image, self.rect)
        elif self.directionx == 1 and self.directiony == -1:
            screen.blit(self.up_right_image, self.rect)
        elif self.directionx == 1 and self.directiony == 1:
            screen.blit(self.down_right_image, self.rect)
        elif self.directionx == -1 and self.directiony == -1:
            screen.blit(self.up_left_image, self.rect)
        elif self.directionx == - 1 and self.directiony == 1:
            screen.blit(self.down_left_image, self.rect)
        #elif self.directionx == 1 and self.directiony == 1:
            #screen.blit(self.down_right_image, self.rect)



