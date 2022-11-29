import functools
import pyperclip
import win32.win32gui as win32gui
import threading
from pprint import pprint
from time import sleep
import re

from ja_sentence_segmenter.common.pipeline import make_pipeline  #全てを取りまとめる関数
from ja_sentence_segmenter.concatenate.simple_concatenator import concatenate_matching #
from ja_sentence_segmenter.normalize.neologd_normalizer import normalize #
from ja_sentence_segmenter.split.simple_splitter import split_newline, split_punctuation #行と句読点を管理

split_punc2 = functools.partial(split_punctuation, punctuations=r"、。!?でのをとがはになやも:;,)")
concat_tail_no = functools.partial(concatenate_matching, former_matching_rule=r"", remove_former_matched=False)#^(?P<result>.+)(の)$
segmenter = make_pipeline(normalize, split_newline, concat_tail_no, split_punc2)

def return_seg(text):
    lst = list(segmenter(text))
    newlst = []
    flag = 0
    rule = re.compile("で、|での|の、|が、|の\?|り、|は、|とは|とが|に、|でき|な、|や、|と、|のに|など|なっ|から|なる|です|なら|なく|ない|やめ|のみ|のが|では|でも|なり|には|ので|のは|なん|にも|もっ|にて|やっ|なか|もの|のの|のか|とも|なの|のか|とて")
    # for i in range(len(lst) - 1):
        # if flag == 0:
        #     if rule.search("".join(lst[i : i+2])):
        #         newlst.append("".join(lst[i:i+2]))
        #         flag = 1
        #     elif rule.search("".join(lst[i-1 : i+1])):
        #         newlst[len(newlst)-1] = newlst[len(newlst)-1] + ("".join(lst[i-1 : i+1]))
        #     else:
        #         newlst.append(lst[i])
        # else:
        #     flag = 0

    i = 0
    while i < len(lst):
        if flag == 0: #前回くっつけなかったら
            if rule.search("".join(lst[i : i+2])) and len(lst) - 1 != i:#+1まででマッチングしたら
                # print(i,len(lst))
                # print("A",newlst,"<=",f"{lst[i]} + {lst[i+1]}")
                # print("----------------------------------")
                newlst.append("".join(lst[i:i+2]))#結合したものを適用
                i += 2
                flag = 1#結合したことを示す
            else:
                # print(i,len(lst))
                # print("B",newlst,"<=",lst[i])
                # print("----------------------------------")
                newlst.append("".join(lst[i]))
                i += 1
        else: #前回くっつけたら
            flag = 0 #くっつけていないことに戻す
            # print(i,len(lst))
            if rule.search("".join(lst[i-1 : i+1])):#-1まででマッチングしたら
                # print(lst[i-1:i+1],"match!!!!")
                # print("C:",newlst,"<=",f"{newlst[len(newlst)-1]}+{lst[i]}")
                # print("----------------------------------")
                newlst[len(newlst)-1] = newlst[len(newlst)-1] + lst[i]#新規文字列の末尾に、元文字列の-1をくっつける
                i += 1
            else:
                flag = 0 #くっつけていないことに戻す
                # print(lst[i-1:i+1],"nomatch!!!")
                # print("----------------------------------")
#あれがあれでのこれが、これでの、それはどうなったの?ねえ
    print(newlst)
    return newlst
def clip(text):
    text = text.replace("\\n","").replace("\\r","")
    return text


text = clip(pyperclip.paste())


##/////////////////////////////////
##json
import json



class Json_data:
    def __init__(self):
        json_o = open(__file__ + "/../config.json","r")
        self.json_open = json.load(json_o)

        self.interval = self.json_open["interval"]
        self.colors = self.json_open["colors"]
        self.color_index = self.json_open["color_index"]
        self.speed = self.json_open["speed"]
        self.speed_max = self.json_open["speed_max"]
json_data = Json_data()







##//////////////////////////////////
##tkinter

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.overrideredirect(1)
root.geometry(f"800x400+{int(root.winfo_screenwidth()*0.2)}+{int(root.winfo_screenheight()*0.2)}")
root.focus_force()

def back_play(node):
    sleep(1)
    while win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "tk":
        sleep(0.2)
    node.withdraw()
    with open(__file__ + "/../config.json",mode="wt",encoding="utf-8") as f:
        json.dump(json_data.json_open,f,indent=2)
    node.quit()

def button_change(node,root,json_data,p_bar):
    sleep(1)
    prog_len = len(return_seg(text))
    prog = 1
    for c in return_seg(text):
        node.configure(text=c)
        interval = calc_speed(json_data.speed)
        p_bar.configure(value=prog/prog_len)
        print(prog,"/",prog_len)
        sleep(interval)
        prog += 1
    root.withdraw()
    root.quit()

def change_color(node,root,json_data):
    json_data.color_index = (json_data.color_index + 1) % len(json_data.colors)
    node.config(foreground=json_data.colors[json_data.color_index])
    json_data.json_open["color_index"] = json_data.color_index
    root.update()

def calc_speed(num):
    return 10/num/10

def change_speed(node,root,json_data):
    json_data.speed = (json_data.speed + 1 ) % json_data.speed_max
    if json_data.speed == 0:
        json_data.speed = 1
    node.config(text=json_data.speed)
    json_data.json_open["speed"] = json_data.speed
    root.update()


root.update_idletasks()

button_color = tk.Button(root,text="Start",font=("helvetica",25),wraplength=root.winfo_width(),width=root.winfo_height(),height=root.winfo_height(),foreground=json_data.colors[json_data.color_index])
button_color.configure(command=functools.partial(change_color,button_color,root,json_data))

button_speed = tk.Button(root,text=json_data.speed,width=int(root.winfo_width()*0.2),font=("helvetica",25),foreground="black",background="lightgrey")
button_speed.configure(command=functools.partial(change_speed,button_speed,root,json_data))

style=ttk.Style()
style.theme_use("alt")#alt,aqua,clam,classic,default
style.configure("blue.Horizontal.TProgressbar",background="red",bordercolor="None")


progress = ttk.Progressbar(mode="determinate",orient=tk.HORIZONTAL,value=50,maximum=1,length=root.winfo_width(),style="blue.Horizontal.TProgressbar")

button_speed.pack(side=tk.BOTTOM)
button_color.pack(side=tk.BOTTOM)
progress.place(x=0,y=0)

th_back_play = threading.Thread(target=back_play,args=(root,))
th_back_play.daemon = True
th_back_play.start()

th_button_change = threading.Thread(target=button_change,args=(button_color,root,json_data,progress))
th_button_change.daemon = True
th_button_change.start()

root.mainloop()
