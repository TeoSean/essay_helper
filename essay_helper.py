import sounddevice as sd
import numpy as np

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm > 20:
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')

        
    
while True:

    with sd.Stream(callback=print_sound):
        sd.sleep(10000)
