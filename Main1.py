import time
import turtle

import pygame



pygame.init


    
def board_make(white_check):
    screen = pygame.display.set_mode((800, 800))
    screen.fill("blue")
    color_count = white_check
    for y in range (8):
        for x in range (8):
            if color_count%2 == 0:
                pygame.draw.rect(screen, "brown", (x*100, y*100 , 100, 100))
            else:
                pygame.draw.rect(screen, "white", (x*100, y*100 , 100, 100))
            color_count = color_count+1
        color_count = color_count+1
    
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
    
