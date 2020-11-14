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

player=pygame.image.load("cat.png").convert()
cat = pygame.transform.scale(player, (100, 100))
screen.blit(cat, (250, 350))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
