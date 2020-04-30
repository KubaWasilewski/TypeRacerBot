from PIL import ImageGrab
import pytesseract
import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import time
import keyboard as kb
import sys


#box to capture cords:
#top left : (25,450)
#bottom right : (890,510)ain forseh ses Lae)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Kubaw\AppData\Local\Tesseract-OCR\tesseract.exe'
keyboard = Controller()

def execute(sentence):
    sentence.strip()
    sentence = sentence.replace("|","I")
    sentence_char_list = list(map(lambda x: x, sentence))
    for char in sentence_char_list:
        time.sleep(0.02)
        keyboard.press(char)
        keyboard.release(char)
    keyboard.press(Key.space)
    keyboard.release(Key.space)




def imageGrab():
    box = (410,535,1265,580)
    image = ImageGrab.grab(box)
    return image

while True:
    image = imageGrab()
    imageArr = np.array(image)
    cv2.imshow("Window",imageArr)
    key = cv2.waitKey(1)
    if key == ord('q'):
        time.sleep(3)
        cv2.destroyAllWindows()
        break

while True:
    time.sleep(0.02)
    image = imageGrab()
    imageArr = np.array(image)
    text = pytesseract.image_to_string(image,lang="eng")
    execute(text)
    if kb.is_pressed('esc'):
        sys.exit()


#(425 535) full screen top left
#(1270,580) full screen bottom right
