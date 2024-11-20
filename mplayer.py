# Music Player
# By Michael Morales

import os
import pygame
from time import sleep

def show_banner():
    """
    Displays a banner for the music player.
    """
    print("""
    ********************************************
    *      🎵 Michael's Awesome Music Player 🎵    *
    *        Relax, Listen, and Enjoy!         *
    ********************************************
    """)

def load_songs(directory):
    """
    Loads all `.mp3` files from the given directory.
    """
    songs = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    if not songs:
        print("No MP3 files found in the directory!")
        return []
    print("\nSongs loaded:")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")
    return songs

def play_song(directory, song):
    """
    Plays the selected song using pygame.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(directory, song))
    pygame.mixer.music.play()
    print(f"\n🎶 Now playing: {song}")

def music_player():
    """
    Main function to handle music playback.
    """
    show_banner()

    # Get the directory containing the songs
    directory = input("Enter the directory containing your MP3 files: ").strip()

    if not os.path.isdir(directory):
        print("Invalid directory! Please check the path and try again.")
        return

    songs = load_songs(directory)
    if not songs:
        return

    current_index = 0
    play_song(directory, songs[current_index])

    while True:
        print("\nOptions:")
        print("1. Play/Pause")
        print("2. Next")
        print("3. Previous")
        print("4. Stop and Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                print("⏸ Music paused.")
            else:
                pygame.mixer.music.unpause()
                print("▶️ Music resumed.")

        elif choice == "2":
            current_index = (current_index + 1) % len(songs)
            play_song(directory, songs[current_index])

        elif choice == "3":
            current_index = (current_index - 1) % len(songs)
            play_song(directory, songs[current_index])

        elif choice == "4":
            pygame.mixer.music.stop()
            print("\n🎵 Thanks for using Michael's Music Player! Goodbye! 🎵")
            break

        else:
            print("Invalid option! Please choose 1, 2, 3, or 4.")

        sleep(1)

if __name__ == "__main__":
    music_player()
