import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((600, 600))
songs=["Ladyfingers.mp3", "sponge.mp3", "spectre.mp3"]
current_song=0
is_playing=False
pygame.mixer.music.load(songs[current_song])
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing=False
                else:
                    pygame.mixer.music.play()
                    is_playing=True
            elif event.key==pygame.K_s:
                pygame.mixer.music.stop()
                is_playing=False
            elif event.key==pygame.K_RIGHT:
                current_song=(current_song+1)%len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                is_playing=True
            elif event.key==pygame.K_LEFT:
                current_song=(current_song-1)%len(songs)
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                is_playing=True
    if not pygame.mixer.music.get_busy() and is_playing:
        is_playing=False
        current_song=(current_song+1)%len(songs)
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()
        is_playing=True
    pygame.display.flip()
