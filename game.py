import pygame
import random
import sys
from shooter import Shooter
from enemy import Enemy
from bullet import Bullet

from missile_diagonal import Missile_diagonal
from walls import walls, add_walls


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('assets/rocket.wav')
pygame.mixer.music.load('assets/background_music.wav')
pygame.mixer.music.play(-1)

bullet_sound = pygame.mixer.Sound('assets/flocka.wav')
loser_sound = pygame.mixer.Sound('assets/loser_audio.wav')


clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600

# game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

color = (100, 200, 230)
screen.fill(color)
pygame.display.update()

add_walls()

background = pygame.image.load("assets/full_background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


shooters = pygame.sprite.Group()


shooter = Shooter(20, 30)
enemy = Enemy(200, 200)
shooter2 = Shooter(450, 250)

bg = pygame.image.load("assets/full_background.png")
background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
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

            #shooters bullet creation logic
            if event.key == pygame.K_SPACE:
                if shooter.image != shooter.loser_image:
                    bullet_sound.play()
                else:
                    loser_sound.play()
                directionx = 1
                directiony = 0
                if shooter.image == shooter.right_image:
                    directionx = 1
                    directiony = 0
                elif shooter.image == shooter.left_image:
                    directionx = -1
                    directiony = 0
                elif shooter.image == shooter.up_image:
                    directiony = -1
                    directionx = 0
                elif shooter.image == shooter.down_image:
                    directiony = 1
                    directionx = 0
                elif shooter.image == shooter.down_right_image:
                    directionx = 1
                    directiony = 1
                elif shooter.image == shooter.down_left_image:
                    directionx = -1
                    directiony = 1
                elif shooter.image == shooter.up_right_image:
                    directionx = 1
                    directiony = -1
                elif shooter.image == shooter.up_left_image:
                    directionx = -1
                    directiony = -1
                elif shooter.image == shooter.loser_image:
                    directionx = 0
                    directiony = 0
                new_bullet = Bullet(shooter.rect.centerx, shooter.rect.centery,directionx, directiony)  # Replace with the actual Bullet class
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
            if event.key == pygame.K_SPACE and shooter.image == shooter.loser_image:
                loser_sound.play()
            if event.key == pygame.K_x and shooter2.image == shooter2.loser_image:
                loser_sound.play()


           #Functionality of shooter 2's missiles
            if event.key == pygame.K_x:
                if shooter2.image != shooter2.loser_image:
                    sound.play()
                else:
                    loser_sound.play()
                directionx = 1
                directiony = 0
                if shooter2.image == shooter2.right_image:
                    directionx = 1
                    directiony = 0
                elif shooter2.image == shooter2.left_image:
                    directionx = -1
                    directiony = 0
                elif shooter2.image == shooter2.up_image:
                    directionx = 0
                    directiony = -1
                elif shooter2.image == shooter2.down_image:
                    directionx = 0
                    directiony = 1
                elif shooter2.image == shooter2.down_right_image or (shooter2.moving_down == True and shooter2.moving_right == True):
                    directionx = 1
                    directiony = 1
                elif shooter2.image == shooter2.down_left_image:
                    directionx = -1
                    directiony = 1
                elif shooter2.image == shooter2.up_right_image:
                    directionx = 1
                    directiony = -1
                elif shooter2.image == shooter2.up_left_image:
                    directionx = -1
                    directiony = -1
                elif shooter2.image == shooter2.loser_image:
                    directionx = 0
                    directiony = 0
                new_missile_diagonal = Missile_diagonal(shooter2.rect.centerx, shooter2.rect.centery, directionx, directiony)  # Replace with the actual Bullet classx
                missiles.add(new_missile_diagonal)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                shooter2.moving_left = False
            if event.key == pygame.K_d:
                shooter2.moving_right = False
            if event.key == pygame.K_w:
                shooter2.moving_up = False
            if event.key == pygame.K_s:
                shooter2.moving_down = False
    #collision functions of the missiles and shooters
    collisions = pygame.sprite.spritecollide(shooter, missiles, True)
    if len(collisions) >= 1 and shooter.health >= 10:
        shooter.health -= 7
        print(shooter.health)
    elif len(collisions) >= 1 and shooter.health <= 5:
        shooter.health += 0
        print (shooter.health)

    #bullet collision and damage logic
    collisions = pygame.sprite.spritecollide(shooter2, bullets, True)
    if len(collisions) >= 1 and shooter2.health >= 10:
        shooter2.health -= 6
    elif len(collisions) >= 1 and shooter2.health <= 5:
        shooter2.health += 0

    #makes it so bullets cannot shoot through some buildings and game objects
    for wall in walls:
        pygame.sprite.spritecollide(wall, bullets, True)
        pygame.sprite.spritecollide(wall, missiles, True)

    collisions = pygame.sprite.spritecollide(enemy, missiles, True)
    if len(collisions) >= 1:
        shooter2.health += 10
        print(shooter2.health)



    screen.blit(background, (0, 0))
    enemy.update()
    shooter.update()
    shooter2.update()
    bullets.update()
    missiles.update()
    if shooter2.health <= 25:
        enemy.image = pygame.transform.scale(pygame.image.load("assets/fighter.png"), (50,50))
        enemy.update()
        enemy.update()
        shooter.update()
        shooter.update()
        missiles.speed = 4
        missiles.update()
    elif shooter2. health >= 25:
        enemy.image = pygame.transform.scale(enemy.image, (0,0))
    enemy.enemy_AI(shooter)
    shooter.draw(screen)
    shooter2.draw(screen)
    enemy.draw(screen)
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
