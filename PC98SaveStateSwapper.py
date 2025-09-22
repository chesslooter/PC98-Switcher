import pyautogui
import pydirectinput
import time
import random
import os, sys
from KeyCodes import *
from ctypes import *
from audio_player import AudioManager
import keyboard
import threading

GAME_DURATION_LOW = 5
GAME_DURATION_HIGH = 20
# NUMBER_OF_GAMES = 4
remaining_slots = [0, 1, 2, 3]

stop_thread = threading.Event()
sleep_time = 0.1

APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
path = os.path.join(APP_FOLDER, "se_timeout.wav")
audio_manager = AudioManager()

current_slot = -1
new_slot = -1
multiple_slots_remain = True
last_spacebar = 0  # The time when the last spacebar interrupt occurred
last_swap = 0  # The time when the last game swap happened
SPACEBAR_COOLDOWN = 2  # Cooldown time for the spacebar interrupt, in seconds

def swap_slots(current_slot, new_slot):
    print("Switching to slot {}".format(new_slot))
    save_slot = "num{}".format(current_slot + 5)
    load_slot = 'num{}'.format(new_slot)

    audio_manager.play_audio(path, True)
    time.sleep(1)

    pydirectinput.write(['escape'])

    pydirectinput.keyUp('z')
    pydirectinput.keyUp('x')
    pydirectinput.keyUp('shiftleft')
    pydirectinput.keyUp('up')
    pydirectinput.keyUp('down')
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('right')

    pyautogui.press(save_slot)
    pyautogui.press(load_slot)

    pydirectinput.write(['escape'])

def swap_game():
    global current_slot, new_slot, multiple_slots_remain, last_swap, remaining_slots

    if len(remaining_slots) > 1:
        while True:
            rand_num = random.randint(0, len(remaining_slots) - 1)
            new_slot = remaining_slots[rand_num]
            if new_slot != current_slot:
                break
        
        swap_slots(current_slot, new_slot)
        current_slot = new_slot

    elif len(remaining_slots) == 1 and multiple_slots_remain:
        multiple_slots_remain = False
        new_slot = remaining_slots[0]
        # audio_manager.play_audio("Final Speedrun.mp3",False,False)
        print("Final Game")
        swap_slots(current_slot, new_slot)
        current_slot = new_slot

    elif len(remaining_slots) == 0: #Challenge complete.
        # audio_manager.play_audio("You Have Completed The Challenge.mp3",False,False)
        print("Challenge complete. Exiting...")
        os._exit(1)

    # Wait random amount of time
    random_time = random.randint(GAME_DURATION_LOW, GAME_DURATION_HIGH) * (1/sleep_time)  # Multiply by inverse of sleep_time. We do this so that we can run this function every 0.1 seconds instead of every second, to make it feel more responsive
    for i in range(int(random_time)):  # Make sure to cast to an int, as it could be a float
        if stop_thread.is_set():
            break
        time.sleep(sleep_time)
    
    last_swap = time.time()  # Store the current time

# Runs on separate thread and alerts swap_game() if 'b' is pressed
def keyboard_listener():
    global last_spacebar, current_slot, last_swap, remaining_slots
    while True:
        if keyboard.is_pressed('b'):
            if time.time() - last_swap >= 1 and time.time() - last_spacebar >= SPACEBAR_COOLDOWN:  # Check if enough time has passed since the last game swap, and if enough time has passed since the last spacebar interrupt
                last_spacebar = time.time()  # Store the current time
                if current_slot in remaining_slots:
                    remaining_slots.remove(current_slot)  # Remove current_slot from unfinished_slots
                    print(f"Removed {current_slot} from unfinished_slots")
                    stop_thread.set()  # Signal the other thread to stop
                # if len(remaining_slots) > 1:
                #     # This plays anytime you remove a run from the list
                #     # Feel free to change this to whatever sound you want
                #     audio_manager.play_audio("Speedrun Complete.mp3",False,False)
                break
        time.sleep(0.05)

print("\nPRESS B TO BEGIN!")
# audio_manager.play_audio("Press Spacebar To Begin.mp3", False)
keyboard.wait('b')

# audio_manager.play_audio("Starting in 3 2 1.mp3", False)
countdown = 3
while countdown > 0:
    print(f"\nSTARTING IN {countdown}")
    countdown -= 1
    time.sleep(1)

pyautogui.press('num0')

while True:
    stop_thread.clear()
    listener = threading.Thread(target=keyboard_listener)
    listener.start()

    swap_game()

    while listener.is_alive():  
        # the listener thread is still waiting for the b, so let's start a new game
        stop_thread.clear()
        swap_game()