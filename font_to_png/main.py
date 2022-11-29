import os
from PIL import ImageDraw, Image, ImageFont
import numpy as np
import cv2
from pprint import pprint
import matplotlib.pyplot as plt

def show_all_font():
    d = os.environ.get("WINDIR")
    fonts_d = os.path.join(d, "fonts")
    print(fonts_d)
    dirs = [i for i in os.walk(fonts_d)]
    pprint(dirs,indent=2,width=40,compact=True)

def set_font_info(font_family,font_size):
    return {"font_path":font_family,
            "font_size":font_size}

def draw_text(font_path,font_size):
    image = Image.new("RGBA",(200,200),"white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path,font_size)
    draw.text((0,0),
    f"{font_path}\nsample text\nfont_size:{font_size}",
    font=font,
    fill="black")
    return image

def pil_to_numpy(image):# pil_image converts to numpy_arg
    img_numpy = np.asarray(image)
    img_numpy_bgr = cv2.cvtColor(img_numpy, cv2.COLOR_RGBA2BGR)
    return img_numpy_bgr

def show_image(image):
    img_numpy_bgr =  pil_to_numpy(image)
    cv2.imshow("window title", img_numpy_bgr)
    # plt.imshow(image)
    # plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    font = set_font_info("misaki_gothic.ttf",30)
    image = draw_text(font["font_path"],font["font_size"])
    show_image(image)

main()
show_all_font()
