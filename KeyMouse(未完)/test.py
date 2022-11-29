import keyboard as kb
import mouse
def on_press(key):
    print(key.name,kb.key_to_scan_codes(key.name))
def hello():
    print("CALLED!!!!")

# kb.add_hotkey("a",hello,trigger_on_release=True)
mouse.press()
kb.call_later(mouse.release,delay=3)
kb.wait("esc")

#shift 42
#shift 54
#ctrl 29
