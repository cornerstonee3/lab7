import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((1000,1000))
x,y=1000//2, 1000//2
radius=25
speed=20
color=(255, 0, 0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed

    # Clamp position so ball stays fully visible
    x = max(radius, min(1000 - radius, x))
    y = max(radius, min(1000 - radius, y))

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    pygame.time.Clock().tick(30)
