import platform
import ctypes
import os
import sys
# import gconf
import wget
from PIL import Image

def get_wall(wall_type):
    url = 'https://i.imgur.com/WpZuQvO.png'
    # 'https://ih0.redbubble.net/image.702318777.9332/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg'
    if wall_type == 'Windows':
        wall_path = 'C://Users/Public/hen.jpg'
        if os.path.isfile(wall_path):
            os.remove(wall_path)
        wget.download(url, wall_path)
        # stretch_wall(wall_path)
    elif wall_type == 'Linux':
        wall_path = 'hoem/caleb/test_downloads/hen.jpg'
        if os.path.isfile(wall_path):
            os.remove(wall_path)
        wget.download(url, wall_path)
        # stretch_wall(wall_path)
    else:
        print("get_wall_error")
    return wall_path


# TODO: no matter what size I use, same on desktop
def stretch_wall(wall_path):
    image = Image.open(wall_path)
    image = image.resize((200, 200), Image.ANTIALIAS)
    os.remove(wall_path)
    image = image.save(wall_path)


def retract(wall_type):
    if wall_type == 'Windows':
        windows_breacher('C://Users/kmcho/OneDrive/Pictures/dokkaebi_drawing.png')
    elif wall_type == 'Linux':
        print("unavailable")
    elif wall_type == 'Darwin':
        print("unavailable")
    else:
        print("retract_error")


def breach_wall():
    startup = input("start \n")
    if startup == 'k':
        set_wallpaper()
    elif startup == 'r':
        wall_type = platform.system()
        print("retracting...")
        retract(wall_type)
        print("retracted.")
    else:
        print("breach_wall_error")


def gnome_breacher(wall_path):
    system('gsettings set org.gnome.desktop.background picture-uri file:///home/caleb/test_downloads/hen.jpg')


def windows_breacher(wall_path):
    wall_path = os.path.normpath(wall_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_path, 0)


def set_wallpaper():
    wall_type = platform.system()
    print("getting wall...")
    wall_path = get_wall(wall_type)
    print("\n got it.")
    print("breaching wall...")
    if wall_type == 'Windows':
        windows_breacher(wall_path)
        print("wall breached.")
    elif wall_type == 'Linux':
        gnome_breacher(wall_path)
        print("wall breached.")
    elif wall_type == 'Darwin':
        print("unavailale")
    else:
        print("set_wallpaper_error")

