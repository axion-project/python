import curses
import time

cat = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

def animate_cat(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    screen.timeout(100)

    # Initial position and direction
    pos_x, pos_y = 5, 10
    direction = 1

    while True:
        screen.clear()

        # Display the cat at the current position
        for i, line in enumerate(cat.splitlines()):
            screen.addstr(pos_y + i, pos_x, line)

        # Add some funny text under the cat
        screen.addstr(pos_y + 4, pos_x, "Feed me hooman!")

        # Move the cat horizontally
        pos_x += direction
        if pos_x >= curses.COLS - len(cat.splitlines()[0]) or pos_x <= 0:
            direction *= -1

        # Refresh the screen
        screen.refresh()

        # Quit if a key is pressed
        if screen.getch() != -1:
            break

        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(animate_cat)