import pygame

pygame.init()
pygame.mixer.music.load('alone.mp3')
pygame.mixer.music.play()
pygame.event.wait()
