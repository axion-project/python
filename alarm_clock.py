# Alarm Clock
# By Michael Morales

import time
import datetime
import os
from playsound import playsound

def show_banner():
    """
    Displays a welcome banner for the alarm clock.
    """
    print("""
    ***************************************
    *         Michael's Alarm Clock        *
    *      Wake up, it's time to shine!    *
    ***************************************
    """)

def get_alarm_time():
    """
    Prompts the user to enter the alarm time in HH:MM format.
    """
    while True:
        alarm_time = input("Enter the alarm time (HH:MM in 24-hour format): ")
        try:
            valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
            return valid_time.time()
        except ValueError:
            print("Invalid format! Please enter time as HH:MM (e.g., 07:30).")

def alarm_ring():
    """
    Plays an alarm sound when the time is reached.
    """
    print("\n⏰ WAKE UP! It's time! ⏰")
    print("Playing alarm sound...")
    
    # Replace with the path to your alarm sound file
    alarm_sound = "alarm.mp3"
    
    if os.path.exists(alarm_sound):
        playsound(alarm_sound)
    else:
        print("Beep! Beep! (Alarm sound file not found!)")

def main():
    """
    Main function to set and activate the alarm clock.
    """
    show_banner()
    
    # Get the alarm time
    alarm_time = get_alarm_time()
    print(f"\nAlarm set for {alarm_time}. Waiting...")
    
    # Keep checking the current time
    while True:
        now = datetime.datetime.now().time()
        if now >= alarm_time:
            alarm_ring()
            break
        time.sleep(10)  # Check every 10 seconds to save resources

if __name__ == "__main__":
    main()
