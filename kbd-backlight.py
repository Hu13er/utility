#!/usr/bin/python
# Keyboard Backlight
# 

import sys

MAGIC_FILE_ADDR = "/sys/class/leds/smc::kbd_backlight/brightness"

def get_keyboard_backlight():
    with open(MAGIC_FILE_ADDR, 'r') as f:
        return int(f.read().strip())

def set_keyboard_backlight(value):
    with open(MAGIC_FILE_ADDR, 'w') as f:
        f.write(str(value))

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(get_keyboard_backlight())
        sys.exit(0)

    if sys.argv[1] == 'inc':
        value = 10 if len(sys.argv) <= 2 else int(sys.argv[2])
        set_keyboard_backlight(get_keyboard_backlight() + value)
    elif sys.argv[1] == 'dec':
        value = 10 if len(sys.argv) <= 2 else int(sys.argv[2])
        set_keyboard_backlight(get_keyboard_backlight() - value)
    elif sys.argv[1] == 'get':
        print(get_keyboard_backlight())
    elif sys.argv[1] == 'set':
        set_keyboard_backlight(sys.argv[2])

