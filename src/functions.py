"""contains methods for communicating with adb"""

import subprocess
from Tkinter import *
import gui
import create_input_box


def restart_adb():
    """Restart ADB"""
    gui.status_bar.config(text="Restarting ADB...")
    command = "adb usb"
    a = subprocess.call(command)
    if a == 1:
        gui.status_bar.config(text="error: no devices/emulators found")
    elif a == 0:
        gui.status_bar.config(text="ADB successfully restarted")


def reload_devices():
    """Reload List of Devices"""
    command="adb devices"
    a = subprocess.call(command)
    ### incomplete ###


def set_adb_path(master):
    """Set path for adb in local machine"""
    # from main import root
    create_input_box.create_entry("Set ADB Path", "Enter directory which contains adb.exe", master, 0)
    # del root
