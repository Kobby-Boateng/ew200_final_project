import pygame

class Missile_up(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 4
        self.image = pygame.image.load("assets/missile.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.up_image = pygame.transform.rotate(self.image, 90)
        self.down_image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

    def update(self):
        self.rect.y += self.speed * self.direction

    def draw(self, screen):
        if self.direction == 1:
            screen.blit(self.down_image, self.rect)
        elif self.direction == -1:
            screen.blit(self.up_image, self.rect)


