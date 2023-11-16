import pygame
import random
import sys
from shooter import Shooter
import math



pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600


#game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

color = (100,200,230)
screen.fill(color)
pygame.display.update()

background = pygame.image.load("assets/full_background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
self_image = pygame.image.load("assets/tile.png")
self_image = pygame.transform.scale(self_image, (50, 50))
shooter = Shooter(20,30)

bg = pygame.image.load("assets/full_background.png")
background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
self_image = pygame.image.load("assets/tile.png")
self_image = pygame.transform.scale(self_image, (50, 50))

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                shooter.moving_left = False
            if event.key == pygame.K_RIGHT:
                shooter.moving_right = False
            if event.key == pygame.K_UP:
                shooter.moving_up = False
            if event.key == pygame.K_DOWN:
                shooter.moving_down = False
    shooter.update()



    screen.blit(background,(0,0))
    screen.blit(self_image, (100,100))
    shooter.draw(screen)
    pygame.display.update()





#Things to keep true
#1. Retrieve events using a for loop
#2. to get the screen to show something you need to flip the display - display.flip
#3. use clock.tick to continue displaying a consistent background
# to have an active game stick update object between 1 and 2 and then draw the object after updating it