import pygame
from pygame import mixer
mixer.init()

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
done = False
#song
pygame.mixer.music.load("IntroSong.mp3")
pygame.mixer.music.play(-1)

#game logo and name      
pygame.display.set_caption("CatZombie The Game")
icon=pygame.image.load("cat-mask.png")
pygame.display.set_icon(icon)

#wallpaper
#image=pygame.image.load("grass.jpg").convert()
#screen.blit(image, (0, 0))

#player image and position
playerpos=(250, 350)
playerImg=pygame.image.load("cat.png").convert()
player = pygame.transform.scale(playerImg, (100, 100))
screen.blit(player, playerpos)

keys = [False, False, False, False]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    keys[0]=False
                elif event.key==K_a:
                    keys[1]=False
                elif event.key==K_s:
                    keys[2]=False
                elif event.key==K_d:
                    keys[3]=True

            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=True
                elif event.key==pygame.K_a:
                    keys[1]=False
                elif event.key==pygame.K_s:
                    keys[2]=False
                elif event.key==pygame.K_d:
                    keys[3]=False
                
            done = True
    pygame.display.flip()

    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
