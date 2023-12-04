import pygame
import shooter
from shooter import bullets


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image,self.rect)

walls = pygame.sprite.Group()

for wall in walls:
    pygame.sprite.spritecollide(wall, bullets, True)
for wall in walls:
    pygame.sprite.spritecollide(wall, shooter, False)

def add_walls():
    walls.add(Wall(45, 70, 40, 30))
    walls.add(Wall(180, 100, 50, 40))
    walls.add(Wall(315, 105 ,50,35))
    walls.add(Wall(360,140,50,35))
    walls.add(Wall(405,175,50,45))
    walls.add(Wall(315, 180 ,50,35))
    walls.add(Wall(180, 185, 50, 30))
    walls.add(Wall(540,175,50,45))
    walls.add(Wall(625,175,50,45))





