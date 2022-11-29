from janome.tokenizer import Tokenizer
from tkinter import ttk
import functools
import pyperclip
import win32.win32gui as win32gui
import threading
from pprint import pprint
from time import sleep
import re
import json
import tkinter as tk


### split by segments
def split_string():
    string = clip(pyperclip.paste())
    t = Tokenizer()
    str_list = t.tokenize(string)
    return str_list

def clip(text):
    text = text.replace("\\n","").replace("\\r","").replace(" ","")
    return text



### JSON
class J_obj:
    def __init__(self):
        json_o = open(__file__ + "/../config.json","r")
        self.json_open = json.load(json_o)
        self.filepath = __file__ + "/../config.json"
        self.interval = self.json_open["interval"]
        self.colors = self.json_open["colors"]
        self.color_index = self.json_open["color_index"]
        self.speed = self.json_open["speed"]
        self.speed_max = self.json_open["speed_max"]
        self.interval = self.speed / 60
    def dump(self):
        with open(self.filepath,mode="wt",encoding="utf-8") as f:
            json.dump(self.json_open,f,indent=2)
    def get_color(self):
        return self.colors[self.color_index]
    def change_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.json_open["color_index"] = self.color_index
    def get_speed(self):
        return self.speed
    def change_speed(self):
        self.speed = (self.speed + 50) % self.speed_max
        if self.speed == 0:
            self.speed = 50
        self.interval = self.speed / 60
        self.json_open["speed"] = self.speed
    def get_interval(self):
        return self.interval

### Tkinter

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(1)
        self.root.geometry(f"800x400+{int(self.root.winfo_screenwidth()*0.2)}+{int(self.root.winfo_screenheight()*0.2)}")
        self.root.focus_force()
    def back_play(self,j_obj):
        sleep(1)
        while win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "tk":
            sleep(0.2)
        self.root.withdraw()
        j_obj.dump()
        self.root.quit()

class Button():
    def __init__(self,text="",font=("helvetica",10),wraplength=0,width=0,height=0,fg="None",bg="None"):
        self.button = tk.Button(self,
                           text=text,
                           font=font,
                           wraplength=wraplength,width=width,height=height,
                           fg=fg,bg=bg,
                           command=functools.partial(self.change_color,app.root,j_obj))
    def change_word(self,text):
        self.button.configure(text=text)
    def change_color(self,root,j_obj):
        j_obj.change_color()
        self.button.configure(fg=j_obj.get_color())
        root.update()
    def change_speed(self,root,j_obj):
        j_obj.change_speed()
        self.button.configure(text=j_obj.get_speed())
        root.update()


class Progress():
    def __init__(self,root,prog_len):
        self.progress = ttk.Progressbar(mode="determinate",orient=tk.HORIZONTAL,value=50,maximum=1,length=root.winfo_width(),style="blue.Horizontal.TProgressbar")
        self.prog_len = prog_len
        self.prog_index = 1
    def change_progress(self):
        self.progress.configure(value=self.prog_index/self.prog_len)
        self.prog_index += 1


def run(text_button,root,j_obj,progress):
    sleep(1)
    str_list = split_string()
    for c in str_list:
        text_button.change_word(c)
        progress.change_progress()
        sleep(j_obj.get_interval())
    root.withdraw()
    j_obj.dump()
    root.quit()

### main

app = App()
j_obj = J_obj()
text_button = Button(text="Start",
                     font=("helvetica",25),
                     wraplength=app.root.winfo_width(),
                     width=app.root.winfo_width(),
                     height=app.root.winfo_height(),
                     fg=j_obj.get_color())
color_button = Button(text=j_obj.get_speed(),
                      font=("helvetica",25),
                      height=int(app.root.winfo_height()*0.2),
                      width=app.root.winfo_width())

style=ttk.Style()
style.theme_use("alt")#alt,aqua,clam,classic,default
style.configure("blue.Horizontal.TProgressbar",background="red",bordercolor="None")
progress = Progress(app.root,3000)


color_button.button.pack(side=tk.BOTTOM)
text_button.button.pack(side=tk.BOTTOM)
progress.progress.place(x=0,y=0)
