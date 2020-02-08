import platform
import ctypes
import os
import sys
# import gconf
import wget
from PIL import Image
import schedule
import time


def get_wall(wall_type):
    origin = 'get_wall'
    try:
        url = 'https://ih0.redbubble.net/image.702318777.9332/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg'
        # blocked by school firewall
        # 'https://i.imgur.com/WpZuQvO.png'
        if wall_type == 'Windows':
            wall_path =  get_home_dir(wall_type)+'/hen.jpg'
            if os.path.isfile(wall_path):
                os.remove(wall_path)
            wget.download(url, wall_path)
            stretch_wall(wall_path)
        elif wall_type == 'Linux':
            wall_path = get_home_dir(wall_type)+'/hen.jpg'
            if os.path.isfile(wall_path):
                os.remove(wall_path)
            wget.download(url, wall_path)
            # stretch_wall(wall_path)
        else:
            print("input_error")    
        return wall_path
    except:
        get_error(origin)


def stretch_wall(wall_path):
    image = Image.open(wall_path)
    width, height = image.size
    if width <= 800 and height <= 800:
        image = image.resize((800, 800), Image.ANTIALIAS)
        os.remove(wall_path)
        image = image.save(wall_path)


# TODO: revert in future
def retract(retract_type):
    origin = 'retract'
    try:
        wal_type = platform.system()
        if wall_type == 'Windows':
            if retract_type == 'rr':
                windows_breacher('C://Users/kmcho/OneDrive/Pictures/backgrounds/python.png')
            elif retract_type == 'r':
                windows_breacher('https://s23527.pcdn.co/wp-content/uploads/2017/09/underexposing_the_scene-768x432.jpg.optimal.jpg')
        elif wall_type == 'Linux':
            print("unavailable")
        elif wall_type == 'Darwin':
            print("unavailable")
        else:
            print("input_error")
    except:
        get_error(origin)


def breach_wall():
    origin = 'breach_wall'
    try:
        startup = input("start \n")
        if startup == 'k':
            set_wallpaper()
        elif startup == 'r' or startup == 'rr':
            print("retracting...")
            retract(startup)
            print("retracted.")
        elif startup == 'n':
            print("abort")
        elif startup == 'at':
            periodic_breach()
        else:
            print("input_error")
    except:
        get_error(origin)


# TODO: check if this works
def periodic_breach():
    set_wallpaper()
    # for test, do seconds
    schedule.every().seconds.do(set_wallpaper)
    while True:
        schedule.run_pending()
        # maybe I don't need this? sleep after code execution
        # time.sleep(10)


def gnome_breacher(wall_path):
    try:
        os.system('gsettings set org.gnome.desktop.background picture-uri file://' + wall_path)
    except:
        get_error("gnome_breacher")


def windows_breacher(wall_path):
    origin = 'windows_breacher'
    try:
        wall_path = os.path.normpath(wall_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_path, 0)
    except:
        get_error(origin)


def set_wallpaper():
    origin = 'set_wallpaper'
    try:
        wall_type = platform.system()
        print("getting wall...")
        wall_path = get_wall(wall_type)
        print("\n got it.")
        print("breaching wall...")
        if wall_type == 'Windows':
            try:
                windows_breacher(wall_path)
            except:
                get_error("set_wallpaper")
            print("wall breached.")
        elif wall_type == 'Linux':
            gnome_breacher(wall_path)
            print("wall breached.")
        elif wall_type == 'Darwin':
                print("unavailale")
        else:
            print("input_error")
    except:
        get_error(origin)


def get_home_dir(wall_type):
    if wall_type == 'Windows':
        return os.environ['HOMEDRIVE']+'/Users/Public'
    elif wall_type == 'Linux':
        return os.environ['HOME']
    elif wall_type == 'Darwin':
        return 'Users/'
    else:
        return 'No match'


def get_error(origin):
    e = sys.exc_info()[0]
    # discard if you need to display exit
    if not e == SystemExit:
        print(origin+"_error: %s" % e)
        sys.exit()

