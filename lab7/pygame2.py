import pygame
import os

pygame.mixer.init()

playlist = ["I_Never_Felt_So_Right.mp3", "kuttim_ai.mp3", "nazik_gulim.mp3"]
current_index = 0

def play_song():
    pygame.mixer.music.load(playlist[current_index])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[current_index]}")

def stop_song():
    pygame.mixer.music.stop()
    print("music is stopped")

def next_song():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play_song()

while True:
    command = input("you can write play/stop/next/previous/exit: ").strip().lower()
    if command == "play":
        play_song()
    elif command == "stop":
        stop_song()
    elif command == "next":
        next_song()
    elif command == "previous":
        previous_song()
    elif command == "exit":
        stop_song()
        break
    else:
        print("wrong command")