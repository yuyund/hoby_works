import keyboard as kb
from time import sleep
from matplotlib.backend_bases import MouseEvent
import mouse
from keyMemory import KeyMemory

km = KeyMemory()
class KeyCondition:
    def __init__(self):
        self.key_press = {}
interval = 0.02
double_click=0.18
speed = 25

def test(keycon):
    while True:
        print(keycon.key_press)
        sleep(0.5)

def on_press(key):
    km.add_key_and_time(key.name,key.time)
    if key.name == "変換":
        check_henkan_double()
def mouse_move(keycon):
    [kb.block_key(c) for c in ["f","d","e","s","l",";","v","r"]]
    while kb.is_pressed("変換"):
        speedx = 0
        speedy = 0
        scroll_delta = 0
        speedx += speed if kb.is_pressed("f") == True else 0
        speedx -= speed if kb.is_pressed("s") == True else 0
        speedy += speed if kb.is_pressed("d") == True else 0
        speedy -= speed if kb.is_pressed("e") == True else 0
        scroll_delta += -2 if kb.is_pressed("v") == True else 0
        scroll_delta -= -2 if kb.is_pressed("r") == True else 0
        speedx,speedy,scroll_delta = [speedx*2,speedy*2,scroll_delta*2] if kb.is_pressed(";") == True else [speedx,speedy,scroll_delta]
        speedx,speedy,scroll_delta = [int(speedx*0.5),int(speedy*0.5),int(scroll_delta*0.5)] if kb.is_pressed("l") == True else [speedx,speedy,scroll_delta]
        if keycon.key_press.get("j") == "press":
            keycon.key_press.update({"j":"midnop"})
            mouse.press()
        elif keycon.key_press.get("j") == "release":
            keycon.key_press.update({"j":"prenop"})
            mouse.release()
        if keycon.key_press.get("k") == "press":
            keycon.key_press.update({"k":"midnop"})
            mouse.press(button=mouse.RIGHT)
        elif keycon.key_press.get("k") == "release":
            keycon.key_press.update({"k":"prenop"})
            mouse.release(button=mouse.RIGHT)
        mouse.move(speedx,speedy,absolute=False)
        mouse.wheel(delta=scroll_delta)
        sleep(interval)
    [kb.unblock_key(c) for c in ["f","d","e","s","l",";","v","r"]]
def check_henkan_double():
    if km.is_same_key() == True and km.get_time_gap() < double_click:
        kb.send("半角/全角")

def mouse_press(keycon,key):
    if keycon[0].key_press.get(key.name) == "prenop":
        keycon[0].key_press.update({key.name.lower():"press"})
def mouse_release(keycon,key):
    keycon[0].key_press.update({key.name.lower():"release"})
def scroll_down():
    delta = -2
    delta /= 2 if kb.is_pressed("l") else 1
    delta *= 2 if kb.is_pressed(";") else 1
    mouse.wheel(delta=int(delta))
def scroll_up():
    delta = 2
    delta /= 2 if kb.is_pressed("l") else 1
    delta *= 2 if kb.is_pressed(";") else 1
    mouse.wheel(delta=int(delta))
