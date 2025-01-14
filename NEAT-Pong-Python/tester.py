import pygame
pygame.init()

width, height = 700, 500
window = pygame.display.set_mode((width, height))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    window.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.update()

pygame.quit()