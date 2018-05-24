#!/bin/python
import os

def get_volume():
    outp = os.popen('amixer get Master').read()
    return outp.strip().split('\n')[6].strip().split()[4][1:-1]

def set_volume(inp):
    os.popen('amixer set Master ' + str(inp))

def rm_status():
    os.popen('rm -rf /tmp/mute')

def save_status(status):
    with open("/tmp/mute", 'w') as f:
        f.write(status)

def get_status():
    try:
        with open("/tmp/mute", 'r') as f:
            content = f.read()
            return content if content != "" else None
    except:
        return None


if __name__ == "__main__":
    last_status = get_status()
    if last_status is None:
        save_status(get_volume())
        set_volume(0)
    else:
        set_volume(last_status)
        rm_status()
        
