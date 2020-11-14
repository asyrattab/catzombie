import pygame
from pygame import mixer
mixer.init()

pygame.init()
screen = pygame.display.set_mode((500, 500))
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

player=pygame.image.load("cat.png").convert()
cat = pygame.transform.scale(player, (100, 100))
screen.blit(cat, playerpos)
keys = [False, False, False, False]
playerpos=[250,450]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                keys[0]=True
                elif event.key==K_a:
                keys[1]=True
                elif event.key==K_s:
                keys[2]=True
                elif event.key==K_d:
                keys[3]=True
                if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                keys[0]=False
                elif event.key==pygame.K_a:
                keys[1]=False
                elif event.key==pygame.K_s:
                keys[2]=False
                elif event.key==pygame.K_d:
                keys[3]=False
            done = True
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    pygame.display.flip()
