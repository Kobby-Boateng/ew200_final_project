import pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 4
        self.image = pygame.image.load("assets/missile.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.left_image = self.image
        self.left_image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

    def update(self):
        self.rect.x += self.speed * self.direction

    def draw(self, screen):
        if self.direction == 1:
            screen.blit(self.image, self.rect)
        elif self.direction == -1:
            screen.blit(self.left_image, self.rect)
