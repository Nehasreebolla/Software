import select
import sys
import pygame
import random

def play_song(song, start_time=0.0):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(start=start_time)
    print("Now playing:", song)

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def stop_song():
    pygame.mixer.music.stop()

def get_next_song(songs):
    return random.choice(songs)

def main():
    pygame.mixer.init()
    pygame.init()

    songs = [
        "/home/neha/1.mp3",
        "/home/neha/2.mp3",
        "/home/neha/3.mp3",
        "/home/neha/4.mp3",
        "/home/neha/5.mp3",
        "/home/neha/6.mp3",
        "/home/neha/7.mp3",
        "/home/neha/8.mp3",
        "/home/neha/9.mp3",
        "/home/neha/10.mp3",
        "/home/neha/11.mp3",
        "/home/neha/12.mp3",
        "/home/neha/13.mp3",
        "/home/neha/14.mp3",
        "/home/neha/15.mp3",
        "/home/neha/16.mp3",
        "/home/neha/17.mp3",
        "/home/neha/18.mp3",
        "/home/neha/19.mp3",
        "/home/neha/20.mp3"
    ]

    current_song = get_next_song(songs)
    play_song(current_song)

    is_paused = False
    paused_song = None
    paused_time = 0.0

    while True:
        ready, _, _ = select.select([sys.stdin], [], [], 1)
        if ready:
            command = input().lower()

            if command == "pause":
                if not is_paused:
                    pause_song()
                    is_paused = True
                    paused_song = current_song
                    paused_time = pygame.mixer.music.get_pos() / 1000.0
            elif command == "resume":
                if is_paused:
                    resume_song()
                    is_paused = False
                    if paused_song:
                        current_song = paused_song
                        paused_song = None
                        play_song(current_song, paused_time)
            elif command == "next":
                stop_song()
                current_song = get_next_song(songs)
                play_song(current_song)
                is_paused = False
                paused_song = None
                paused_time = 0.0
            elif command == "quit":
                stop_song()
                break

        if not pygame.mixer.music.get_busy() and not is_paused:
            current_song = get_next_song(songs)
            play_song(current_song)

    pygame.quit()

if __name__ == "__main__":
    main()
