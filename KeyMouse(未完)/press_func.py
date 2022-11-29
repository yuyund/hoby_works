#from pynput import keyboard,mouse
import keyboard
keyboard.add_hotkey()

class Keypush:
    def __init__(self):
        pass
    def on_press(self,key):
        pass
    def on_release(self,key):
        if key == keyboard.Key.esc:
            return False
        elif key.vk == 28 or key.vk == 29:
            mouse.Controller().move(3,0)
