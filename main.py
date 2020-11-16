import pygame
from game import Game
from pygame import mixer
mixer.init()

g = Game()

pygame.display.set_caption("CatZombie The Game")
icon=pygame.image.load("cat-mask.png")
pygame.display.set_icon(icon)

pygame.mixer.music.load("IntroSong.mp3")
pygame.mixer.music.play(-1)

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

