import math
import utime
import picounicorn

picounicorn.init()

test_mode = True

RED = {
    "r":255,
    "g":0,
    "b":0,
}
GREEN = {
    "r":0,
    "g":255,
    "b":0,
}
BLACK = {
    "r":0,
    "g":0,
    "b":0,
}
WIDTH = picounicorn.get_width()
HEIGHT = picounicorn.get_height()
TOTAL_PIXELS = HEIGHT * WIDTH
WORK_SECONDS = 25 * 60 if not test_mode else 25
BREAK_SECONDS = 5 * 60 if not test_mode else 5

def fill_screen(colour):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            picounicorn.set_pixel(x, y, colour['r'], colour['g'], colour['b'])


def pomodero():
    colour = RED
    phase = "work"
    countdown_seconds = WORK_SECONDS

    while not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):
        fill_screen(colour)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                if not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):
                    picounicorn.set_pixel(x, y, 0, 0, 0)
                    utime.sleep(countdown_seconds/TOTAL_PIXELS)
                else:
                    fill_screen(BLACK)
                    break
                
        
        if phase == "work":
            phase = "break"
            colour=GREEN
            countdown_seconds = BREAK_SECONDS
        elif phase == "break":
            phase = "work"
            colour=RED
            countdown_seconds = WORK_SECONDS
        pass


fill_screen(BLACK)
while 1:
    while picounicorn.is_pressed(picounicorn.BUTTON_X):
        pomodero()

