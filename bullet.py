import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, directionx, directiony):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.directionx = directionx
        self.directiony = directiony

    def update(self):
        self.rect.x += self.speed * self.directionx
        self.rect.y += self.speed * self.directiony

    def draw(self, screen):
        screen.blit(self.image, self.rect)
