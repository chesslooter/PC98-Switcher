import pyautogui
import pydirectinput
import time
import random
import os, sys
from KeyCodes import *
from ctypes import *
from audio_player import AudioManager

GAME_DURATION_LOW = 5
GAME_DURATION_HIGH = 20
NUMBER_OF_GAMES = 2

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
path = os.path.join(APP_FOLDER, "se_timeout.wav")
audio_manager = AudioManager()

currentSlot = 0
newSlot = 0

time.sleep(10)
pyautogui.press('num0')
while True:
    while True:
        newSlot = random.randint(0, NUMBER_OF_GAMES - 1)
        if newSlot != currentSlot:
            break
    
    print("Switching to slot {}".format(newSlot))
    saveSlot = "num{}".format(currentSlot + 5)
    loadSlot = 'num{}'.format(newSlot)
    
    audio_manager.play_audio(path, True, False, True)
    time.sleep(1)

    pydirectinput.write(['escape'])

    pydirectinput.keyUp('z')
    pydirectinput.keyUp('x')
    pydirectinput.keyUp('shiftleft')
    pydirectinput.keyUp('up')
    pydirectinput.keyUp('down')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')

    pyautogui.press(saveSlot)
    pyautogui.press(loadSlot)

    pydirectinput.write(['escape'])

    currentSlot = newSlot

    time.sleep(random.randint(GAME_DURATION_LOW, GAME_DURATION_HIGH))



# pydirectinput.moveTo(curr_left_x_mouse, curr_left_y_mouse)  