import pyautogui as p
import keyboard as key
from time import sleep
from pynput.mouse import Controller

start_key = "o"
start_key_2 = "i"
print("Macros starting")
mouse = Controller()
text_to_type = "/ah sell 120000"
text_to_type_2 = "!All check moy Ah Pyzurki oputa po 120k!!!"

def ring():
    sleep(0.2)
    key.press("t")
    sleep(0.2)
    p.typewrite(text_to_type)
    sleep(0.2)
    key.press("enter")

def ring_2():
    sleep(0.2)
    key.press("t")
    sleep(0.2)
    p.typewrite(text_to_type_2)
    sleep(0.2)
    key.press("enter")

while True:
    if key.is_pressed(start_key):
        ring()
    elif key.is_pressed(start_key_2):
        ring_2()