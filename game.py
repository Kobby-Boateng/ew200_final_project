import pygame
import random
import sys
from shooter import Shooter
from enemy import Enemy
from bullet import Bullet
from missile import Missile
from missile_up import Missile_up
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600

# game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

color = (100, 200, 230)
screen.fill(color)
pygame.display.update()

background = pygame.image.load("assets/full_background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
self_image = pygame.image.load("assets/tile.png")
self_image = pygame.transform.scale(self_image, (50, 50))

shooter = Shooter(20, 30)
enemies = Enemy(200, 200)
shooter2 = Shooter(450, 250)

bg = pygame.image.load("assets/full_background.png")
background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
self_image = pygame.image.load("assets/tile.png")
self_image = pygame.transform.scale(self_image, (50X, 50))
bullet_image = pygame.image.load("assets/bullet.png")
bullets = pygame.sprite.Group()
missiles = pygame.sprite.Group()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks for playing my game")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shooter.moving_left = True
            if event.key == pygame.K_RIGHT:
                shooter.moving_right = True
            if event.key == pygame.K_UP:
                shooter.moving_up = True
            if event.key == pygame.K_DOWN:
                shooter.moving_down = True
            if event.key == pygame.K_SPACE:
                if shooter.image == shooter.right_image:
                    direction = 1
                elif shooter.image == shooter.image:
                    direction = -1
                elif shooter.image == shooter.up_image:
                    direction = 0
                elif shooter.image == shooter.down_image:
                    direction = 0
                new_bullet = Bullet(shooter.rect.centerx, shooter.rect.centery,
                                    direction)  # Replace with the actual Bullet class
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                shooter.moving_left = False
            if event.key == pygame.K_RIGHT:
                shooter.moving_right = False
            if event.key == pygame.K_UP:
                shooter.moving_up = False
            if event.key == pygame.K_DOWN:
                shooter.moving_down = False
            # Example bullet creation logic (adjust as needed)
        # shooter2 movement logic
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                shooter2.moving_left = True
            if event.key == pygame.K_d:
                shooter2.moving_right = True
            if event.key == pygame.K_w:
                shooter2.moving_up = True
            if event.key == pygame.K_s:
                shooter2.moving_down = True
            if event.key == pygame.K_x:
                if shooter2.image == shooter2.right_image:
                    direction = 1
                elif shooter2.image == shooter2.image:
                    direction = -1
                new_missile = Missile(shooter2.rect.centerx, shooter2.rect.centery,
                                      direction)  # Replace with the actual Bullet class
                missiles.add(new_missile)

            if event.key == pygame.K_z and (shooter.image == True or shooter2.moving_down == True):
                if shooter2.moving_up == True:
                    direction = -1
                elif shooter2.moving_down == True:
                    direction = 1
                new_missile_up = Missile_up(shooter2.rect.centerx, shooter2.rect.centery, direction)
                print("shooting missile up")
                missiles.add(new_missile_up)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                shooter2.moving_left = False
            if event.key == pygame.K_d:
                shooter2.moving_right = False
            if event.key == pygame.K_w:
                shooter2.moving_up = False
            if event.key == pygame.K_s:
                shooter2.moving_down = False
                #
    shooter.update()
    collisions = pygame.sprite.spritecollide(shooter, missiles, True)
    if len(collisions) >= 1:
        shooter.health -= 10
        print(shooter.health)
    if shooter.health == 0:
        collisions = pygame.sprite.spritecollide(missiles, shooter, True)


    # if pygame.sprite.spritecollide(shooter, enemies, False):
    # shooter.health-=10

    screen.blit(background, (0, 0))
    screen.blit(self_image, (100, 100))

    shooter.update()
    shooter2.update()
    bullets.update()
    missiles.update()
    # pygame.rect.draw(x,y, 5 ,shooter)
    shooter.draw(screen)
    shooter2.draw(screen)
    enemies.draw(screen)
    enemies.enemies_AI(shooter)
    for bullet in bullets:
        bullet.draw(screen)
    for missile in missiles:
        missile.draw(screen)
    pygame.display.update()

# Things to keep true
# 1. Retrieve events using a for loop
# 2. to get the screen to show something you need to flip the display - display.flip
# 3. use clock.tick to continue displaying a consistent background
# to have an active game stick update object between 1 and 2 and then draw the object after updating it
