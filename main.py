import keyboard as kb
from pprint import pprint
import func
from time import sleep
from keyMemory import KeyMemory
from functools import partial

# KeyConditon
keycon = func.KeyCondition()

# TEST
kb.call_later(func.test,(keycon,))


# マウス
kb.add_hotkey("変換",func.mouse_move,(keycon,))
kb.on_press_key("j",partial(func.mouse_press,(keycon,)))
kb.on_release_key("j",partial(func.mouse_release,(keycon,)))
kb.on_press_key("k",partial(func.mouse_press,(keycon,)))
kb.on_release_key("k",partial(func.mouse_release,(keycon,)))
# 十字キー
kb.remap_hotkey("無変換+j","left")
kb.remap_hotkey("無変換+j+shift","shift+left")
kb.remap_hotkey("無変換+k","down")
kb.remap_hotkey("無変換+k+shift","shift+down")
kb.remap_hotkey("無変換+i","up")
kb.remap_hotkey("無変換+i+shift","shift+up")
kb.remap_hotkey("無変換+l","right")
kb.remap_hotkey("無変換+l+shift","shift+right")
kb.remap_hotkey("無変換+:","end")
kb.remap_hotkey("無変換+:+shift","shift+end")
kb.remap_hotkey("無変換+h","home")
kb.remap_hotkey("無変換+h+shift","shift+home")
kb.remap_hotkey("無変換+変換","f10+enter")

# BS ENTER ESC CONTEXET
kb.remap_hotkey("無変換+;","backspace")
kb.remap_hotkey("無変換+space","enter")
kb.remap_hotkey("無変換+e","esc")
kb.remap_hotkey("無変換+w","menu")

#F_Key
kb.remap_hotkey("無変換+1","f1")
kb.remap_hotkey("無変換+2","f2")
kb.remap_hotkey("無変換+3","f3")
kb.remap_hotkey("無変換+4","f4")
kb.remap_hotkey("無変換+5","f5")
kb.remap_hotkey("無変換+6","f6")
kb.remap_hotkey("無変換+7","f7")
kb.remap_hotkey("無変換+8","f8")
kb.remap_hotkey("無変換+9","f9")
kb.remap_hotkey("無変換+0","f10")
# All KEY Func
kb.on_release(func.on_press)
kb.wait()
#i keyのメンバー
# 'device',
# 'event_type',
# 'is_keypad',
# 'modifiers',
# 'name',
# 'scan_code',
# 'time',
# 'to_json']
