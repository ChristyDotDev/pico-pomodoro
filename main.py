import math
import utime
import picounicorn

picounicorn.init()

test_mode = False

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
    phase = "work"

    while not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):
        fill_screen(RED if phase == 'work' else GREEN)
        sleep_per_cycle = WORK_SECONDS/TOTAL_PIXELS if phase == 'work' else BREAK_SECONDS/TOTAL_PIXELS

        for x in range(WIDTH):
            for y in range(HEIGHT):
                if not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):
                    picounicorn.set_pixel(x, y, 0, 0, 0)
                    utime.sleep(sleep_per_cycle)
                else:
                    fill_screen(BLACK)
                    break
                
        if phase == "work":
            phase = "break"
            countdown_seconds = BREAK_SECONDS
        elif phase == "break":
            phase = "work"
            countdown_seconds = WORK_SECONDS
        pass


fill_screen(BLACK)
while 1:
    while picounicorn.is_pressed(picounicorn.BUTTON_X):
        pomodero()

