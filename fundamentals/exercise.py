# Simple activity logger
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController


def control_mouse():
    mouse = MouseController()
    mouse.position = (500,200)

def control_keyboard():
    keyboard = KeyboardController()
    keyboard.type('it works')

control_keyboard()