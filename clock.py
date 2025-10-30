import pygame
import datetime
import sys
pygame.init()
scr=pygame.display.set_mode((1000, 1000))
background=pygame.image.load("base_micky.jpg")
background=pygame.transform.scale(background, (1000, 1000))
right_hand=pygame.image.load("minute.png").convert_alpha()
left_hand=pygame.image.load("second.png").convert_alpha()
center=(500, 500)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    now=datetime.datetime.now()
    second=now.second
    minute=now.minute
    sec_angle=-second*6
    min_angle=-minute*6-second*0.1
    right=pygame.transform.rotate(right_hand, min_angle)
    left=pygame.transform.rotate(left_hand, sec_angle)
    right_rect = right.get_rect(center=center)
    left_rect = left.get_rect(center=center)
    scr.blit(background, (0, 0))
    scr.blit(right, right_rect)
    scr.blit(left, left_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(30)