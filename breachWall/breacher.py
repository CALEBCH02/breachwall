# This breaches walls!
# execute (.exe)
# check env
#   windows
#   ubuntu
#   mac
# get image
#   download
# set image
#   accordingly to env
import platform
import venv
import ctypes
import os
import struct
import subprocess
import sys
# import commands
import gconf

# import win32con

# from appscript import app, mactypes

import wget
from os import walk, getenv, system
from shutil import copyfile
from PIL import Image


### desktop environment begin ###


def get_desktop_environment(self):
    if sys.platform in ["win32", "cygwin"]:
        return "windows"
    elif sys.platform == "darwin":
        return "mac"
    else:  # Most likely either a POSIX system or something not much common
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session is not None:  # easier to match if we doesn't have  to deal with caracter cases
            desktop_session = desktop_session.lower()
            if desktop_session in ["gnome", "unity", "cinnamon"]:
                return desktop_session
            elif desktop_session.startswith("ubuntu"):
                return "unity"
        if os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            if not "deprecated" in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                return "gnome2"
    return "unknown"
### desktop environment end ###


def get_wall(wall_type):
    url = 'https://ih0.redbubble.net/image.702318777.9332/poster,840x830,f8f8f8-pad,1000x1000,f8f8f8.jpg'
        # eye 'https://cdn.arstechnica.net/wp-content/uploads/2016/02/5718897981_10faa45ac3_b-640x624.jpg'
    if wall_type == 'Windows':
        wall_path = 'C://Users/Public/hen.jpg'
        if not os.path.isfile(wall_path):
            wget.download(url, 'C://Users/Public/hen.jpg')
            # wget.download(url, 'C://Users/kmcho/Downloads/hen.jpg')
            # wall_path = 'C://Users/kmcho/Downloads/hen.jpg'
    elif wall_type == 'Linux':
        wall_path = '/home/caleb/test_downloads/hen.jpg'
        if not os.path.isfile(wall_path):
            wget.download(url, '/home/caleb/test_downloads/hen.jpg')
    return wall_path


### retract begin ####
def retract(wall_type):
    if wall_type == 'Windows':
        windows_breacher('C://Users/kmcho/OneDrive/Pictures/dokkaebi_drawing.png')
#### retract end ###


def breach_wall():
    startup = input("start")
    if startup == 'k':
        set_wallpaper()
    elif startup == 'r':
        wall_type = platform.system()
        print("retracting...")
        if startup == 'r':
            retract(wall_type)
            print("retracted!")
        else:
            print("error")
    else:
        print("error")


### gnome breacher begin ###
def gnome_breacher():
    system("gsettings set org.gnome.desktop.background picture-uri file:///home/caleb/test_downloads/eye.jpg")
#### gnome breacher end ###


### windows breacher begin ###
def windows_breacher(file_loc):
    SPI_SETDESKWALLPAPER = 20
    wall_path = os.path.normpath(file_loc)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_path, 0)
### windows breacher end ###


### adaptive breacher begin ####
def set_wallpaper():
    wall_type = platform.system()
    print("getting wall...")
    wall_path = get_wall(wall_type)
    print("got it!")
    print("breaching wall...")
    if wall_type == 'Windows':
        windows_breacher(wall_path)
        print("wall breached!")
    elif wall_type == 'linux':
        gnome_breacher(wall_path)
        print("wall breached!")
    elif wall_type == 'Darwin':
        print("unavailable")
    print(wall_type)

# def get_config_dir(self, app_name=APP_NAME):
#     if "XDG_CONFIG_HOME" in os.environ:
#         confighome = os.environ['XDG_CONFIG_HOME']
#     elif "APPDATA" in os.environ:  # On Windows
#         confighome = os.environ['APPDATA']
#     else:
#         try:
#             from xdg import BaseDirectory
#             confighome = BaseDirectory.xdg_config_home
#         except ImportError:  # Most likely a Linux/Unix system anyway
#             confighome = os.path.join(self.get_home_dir(), ".config")
#     configdir = os.path.join(confighome, app_name)
#     return configdir


def get_home_dir(self):
    if sys.platform == "cygwin":
        home_dir = os.getenv('HOME')
    else:
        home_dir = os.getenv('USERPROFILE') or os.getenv('HOME')
    if home_dir is not None:
        return os.path.normpath(home_dir)
    else:
        raise KeyError("Neither USERPROFILE or HOME environment variables set.")
### adaptive breacher end ####
