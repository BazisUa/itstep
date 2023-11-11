import sqlite3
import requests
from datetime import datetime
from time import sleep
response = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D0%B8/")

response_text = response.text

response_parse = response_text.split("<span>")

coins = []

for item in response_parse:
    if item.startswith("+"):
        for temp in item.split("</span>"):
            if temp.startswith("+") and temp[1].isdigit():
                temp_number = (temp[0] + temp[1] + temp[2])
                coins.append(temp_number)
temp_num = (coins[0])
temp_norm_num = temp_num.replace("&", "°")
connection = sqlite3.connect("sinoptic.sl3", 5)

cur = connection.cursor()

now = datetime.now()
d1 = now.strftime("%d/%m/%Y %H:%M:%S")
city = ("Черкаси")


print(f"Погодна база міста {city} була оновлена.")
cur.execute("DELETE FROM sinoptic where rowid=1;")
cur.execute(f"INSERT INTO sinoptic (temperature) VALUES ('{temp_norm_num}');")
cur.execute(f"UPDATE sinoptic SET date='{d1}' where rowid=1;")
cur.execute(f"UPDATE sinoptic SET city='{city}' where rowid=1;")





connection.commit()

connection.close()
