import random

import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
x, y = 400, 300 
R = 255 # Red
G = 107 # Green
B = 53  # Blue
#ColourChanged = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= 5
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]:    y -= 5
    if keys[pygame.K_DOWN]:  y += 5

    
    # Store previous position to detect movement
    previous_x = x
    previous_y = y
    
    # Invisible walls: 800 - 40 because X is 800 and the rectangle is 40 wide, so it can't go beyond 760.
    # Effectively turning the screen to 760, 560.
    x = max(0, min(x, 800 - 40))
    y = max(0, min(y, 600 - 40))
    
    #if (ColourChanged == False) and (x <= 0 or x >= 800 - 40 or y <= 0 or y >= 600 - 40):

    if (x != previous_x or y != previous_y) and (x <= 0 or x >= 800 - 40 or y <= 0 or y >= 600 - 40):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
       # ColourChanged = True

    screen.fill((11, 13, 16))
    pygame.draw.rect(screen, (R, G, B), (x, y, 40, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()