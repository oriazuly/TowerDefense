import pygame

from constants import *

run = True
pygame.display.set_caption("Tower Defense")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
pygame.quit()

