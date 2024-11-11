import pygame                   #pygame library
import os
import math
from pygame.locals import *     #needed for user input
import random

#initialization
pygame.init()#starts pygame
screen = pygame.display.set_mode((1440, 720)) #creates screen object + size
gx=100
gy=280
dgx=0
dgy=0
tx=random.randint(700 , 1330)
ty=random.randint(0, 410)
ttf=True
bltx=gx
blty=gy
shoot=False
gravity_acceleration = 1
player_health = 30
ghost_health = 100
ghost_attack = 1
jump_force = 0
jump_counter = 0
player_direction = True
bullet_direction = True
bullet_available = True
bullet_attack = 10
dtx = 5
dty = 5
paper_number = 0
my_font=pygame.font.Font('resources/font/nineteen_ninety_three.otf', 32)

# Advanced
# Title
pygame.display.set_caption("One Mind")
# Icon
game_icon = pygame.image.load('resources/images/icon/icon.png')
pygame.display.set_icon(game_icon)

# Game world# Game World
scenes_back = pygame.image.load('resources/images/scenes/back.png')
scenes_back = pygame.transform.scale(scenes_back, (480, 720))

scenes_middle_a = pygame.image.load('resources/images/scenes/middle-ground-a.png')
scenes_middle_a = pygame.transform.scale(scenes_middle_a, (640, 720))
scenes_middle_b = pygame.image.load('resources/images/scenes/middle-ground-b.png')
scenes_middle_b = pygame.transform.scale(scenes_middle_b, (640, 720))

scenes_foreground_a = pygame.image.load('resources/images/scenes/foreground-a.png')
scenes_foreground_a = pygame.transform.scale(scenes_foreground_a, (400, 360))
scenes_foreground_b = pygame.image.load('resources/images/scenes/foreground-b.png')
scenes_foreground_b = pygame.transform.scale(scenes_foreground_b, (400, 360))
scenes_foreground_d = pygame.image.load('resources/images/scenes/foreground-d.png')
scenes_foreground_d = pygame.transform.scale(scenes_foreground_d, (400, 360))

# player
idle_left = pygame.image.load('resources/images/player/idle_frame_1.png').convert_alpha()
idle_left = pygame.transform.scale(idle_left, (100, 100))
idle_right = pygame.transform.flip(idle_left, True, False)

# Bullet
kunai_right_image = pygame.image.load('resources/images/kunai/kunai.png').convert_alpha()
kunai_right_image = pygame.transform.scale(kunai_right_image, (75, 75))
kunai_right_image = pygame.transform.rotate(kunai_right_image, -45)
kunai_left_image = pygame.transform.flip(kunai_right_image, True, False)
kunai_rect = kunai_left_image.get_rect()

# Ghost
ghost_left_image = pygame.image.load('resources/images/ghost.png').convert_alpha()
ghost_left_image = pygame.transform.scale(ghost_left_image, (100, 200))
ghost_right_image = pygame.transform.flip(ghost_left_image, True, False)

# Music
pygame.mixer.music.load('resources/sound/music.mp3')
# TODO: Volume
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)
# Sound
eat_sound = pygame.mixer.Sound('resources/sound/eat.wav')
pygame.mixer.Sound.set_volume(eat_sound, 0.7)
select_sound = pygame.mixer.Sound('resources/sound/select.wav')
pygame.mixer.Sound.set_volume(select_sound, 0.8)
hit_sound = pygame.mixer.Sound('resources/sound/hit.wav')
pygame.mixer.Sound.set_volume(hit_sound, 0.4)
shoot_sound = pygame.mixer.Sound('resources/sound/shoot.wav')
pygame.mixer.Sound.set_volume(shoot_sound, 0.5)

# Wandering Paper Craft
wandering_paper_craft = pygame.image.load(
    'resources/images/wandering_paper_craft/wandering_paper_craft.png').convert_alpha()
wandering_paper_craft = pygame.transform.scale(wandering_paper_craft, (50, 50))
wandering_paper_craft_rect = wandering_paper_craft.get_rect()
wandering_paper_craft_rect.x, wandering_paper_craft_rect.y = random.randint(100, 1300), random.randint(350, 550)

while True:                          #loop needed for window to stay open
    #drawing
    # screen.fill((255,0,0))
    # pygame.draw.circle(screen, (0,0,255), (gx,gy),20)
    # pygame.draw.circle(screen, (0,200,255), (bltx,blty),10)

    # BACKGROUND
    # Back
    screen.blit(scenes_back, (0, 0))
    screen.blit(scenes_back, (480, 0))
    screen.blit(scenes_back, (960, 0))
    # Middle
    screen.blit(scenes_middle_a, (0, 0))
    screen.blit(scenes_middle_b, (640, 0))
    screen.blit(scenes_middle_a, (1280, 0))
    # Foreground
    screen.blit(scenes_foreground_a, (0, 440))
    screen.blit(scenes_foreground_d, (400, 440))
    screen.blit(scenes_foreground_b, (800, 440))
    screen.blit(scenes_foreground_d, (1200, 440))
    # Player
    if player_direction:
        screen.blit(idle_left, (gx, gy))
    else:
        screen.blit(idle_right, (gx, gy))

    if(shoot==True):
        if bullet_direction:
            bltx=bltx-40
        else:
            bltx=bltx+40

        # Bullet
        if bullet_direction:
            screen.blit(kunai_left_image, (bltx, blty))
        else:
            screen.blit(kunai_right_image, (bltx, blty))

    if not (0 < bltx < 1440):
        shoot=False
    if(shoot==False):
        bltx=gx
        blty=gy
        bullet_available = True
    if(ttf==True):  
        # pygame.draw.circle(screen, (0,0,255), (tx,ty),20)
        if dtx < 0:
            screen.blit(ghost_left_image, (tx, ty))
        else:
            screen.blit(ghost_right_image, (tx, ty))
    if(abs(tx-bltx)<=30 and abs((ty + 100)-blty)<=30) and not bullet_available:
        ghost_health -= bullet_attack
        ttf=False
        # tx=random.randint(20, 380)
        ttf=True
        hit_sound.play()
    if abs(tx - gx) < 50 and abs((ty + 100) - gy) < 50:
        player_health -= ghost_attack
    """sc=my_font.render("score : "+ str(score), True, (0,0,255))
    screen.blit(sc, (20,20))"""

    gx=gx+dgx
    if(gx<20):
        gx=20
        dgx=0
    if(gx>1350):
        gx=1350
        dgx=0

    # UI
    # Player
    user_interface_font = pygame.font.Font('resources/font/mouse.otf', 30)
    hit_point = user_interface_font.render("HP", True, (225, 225, 225))
    # Health bar border
    pygame.draw.rect(screen, (55, 55, 55), (40, 640, 500, 30))
    # Health bar fill
    pygame.draw.rect(screen, (75, 75, 75), (45, 645, 490, 20))
    # Health bar red
    health_bar_red_length = int(490 * (player_health / 30))
    pygame.draw.rect(screen, (200, 60, 66), (45, 645, health_bar_red_length, 20))
    # Text: HP
    screen.blit(hit_point, (50, 610))

    # Ghost
    name_font = pygame.font.Font('resources/font/nineteen_ninety_three.otf', 25)
    ghost_name = name_font.render("Ghost", True, (225, 225, 225))
    # Health bar border
    pygame.draw.rect(screen, (55, 55, 55), (170, 40, 1100, 20))
    # Health bar fill
    pygame.draw.rect(screen, (75, 75, 75), (175, 45, 1090, 10))
    # Health bar red
    health_bar_red_length_ghost = int(1090 * (ghost_health / 100))
    pygame.draw.rect(screen, (200, 60, 66), (175, 45, health_bar_red_length_ghost, 10))
    # Text: HP
    screen.blit(ghost_name, (670, 3))

    # Paper Craft
    wonder_paper_craft_ui = pygame.image.load(
        'resources/images/wandering_paper_craft/wandering_paper_craft_UI.png').convert_alpha()
    screen.blit(wonder_paper_craft_ui, (560, 640))
    # Text: Number
    wonder_paper_craft_number = user_interface_font.render(str(paper_number), True, (225, 225, 225))
    screen.blit(wonder_paper_craft_number, (600, 645))

    # Game State
    you_lost = name_font.render("YOU  LOST !", True, (225, 225, 225))
    you_win = name_font.render("YOU  WIN !", True, (225, 225, 225))
    again = name_font.render("PRESS ENTER/RETURN TO TRY AGAIN", True, (225, 225, 225))

    screen.blit(wandering_paper_craft, wandering_paper_craft_rect)

    if player_health <= 0:
        screen.fill('black')
        screen.blit(you_lost, (630, 320))
        screen.blit(again, (470, 370))
        gx, gy = 0, 0
    if ghost_health <= 0:
        screen.fill('black')
        screen.blit(you_win, (640, 320))
        screen.blit(again, (470, 370))
        tx, ty = 0, 0

    if abs(gx - wandering_paper_craft_rect.x) < 50 and abs(gy - wandering_paper_craft_rect.y) < 50:
        wandering_paper_craft_rect.x, wandering_paper_craft_rect.y = random.randint(100, 1300), random.randint(350, 550)
        paper_number += 1
        eat_sound.play()

    pygame.time.wait(5)
    pygame.display.update()

    # PHYSICAL ENGINE
    if gy < 510:
        dgy += gravity_acceleration
        gy += dgy
    else:
        gy = 510
        jump_counter = 0

    gy += jump_force
    if not jump_force == 0:
        jump_force += gravity_acceleration

    tx += dtx
    ty += dty

    if tx < 0 or tx > 1350:
        dtx = -dtx
    if ty < -100 or ty > 410:
        dty = - dty

    #Event control
    for event in pygame.event.get(): #allows you to close window
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #gx -= 10
                dgx=-10
                player_direction = True
            if event.key == pygame.K_RIGHT:
                #gx += 10
                dgx=10
                player_direction = False
            if event.key == K_UP and jump_counter < 1:
                jump_force = -25
                dgy = 0
                jump_counter += 1
            if event.key == pygame.K_SPACE and bullet_available and paper_number > 0:
                shoot=True
                bullet_available = False
                bullet_direction = player_direction
                paper_number -= 1
                shoot_sound.play()
            if event.key == pygame.K_RETURN and player_health <= 0:
                player_health = 30
                ghost_health = 100
                tx = random.randint(700, 1330)
                ty = random.randint(0, 410)
                gx = 100
                gy = 280
                paper_number = 0
                ghost_attack = 1
                bullet_attack = 19
                dtx = 5
                dty = 5

            elif event.key == pygame.K_RETURN and ghost_health <= 0:
                gx = 100
                gy = 280
                ghost_health = 100
                paper_number = 0
                player_health = 30
                tx = random.randint(700, 1330)
                ty = random.randint(0, 410)
                if bullet_attack > 0:
                    bullet_attack -= 1
                ghost_attack += 2
                dtx += 2
                dty += 2
                select_sound.play()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dgx = 0
        if event.type == QUIT:
            os._exit(1)
