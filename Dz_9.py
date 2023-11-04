import requests

response = requests.get("https://api.monobank.ua/bank/currency")

response_text = response.text
dollar = (response_text[101] + response_text[102] + response_text[103] + response_text[104] + response_text[105] + response_text[106] + response_text[107])
print("Курс доллара США: " + dollar + " ₴")
while True:
    print("")
    user_number = int(input("Кількість Гривнень:"))

    user_number_rate = float(dollar.replace(",", ""))
    dollar_number = user_number / user_number_rate
    print("Ви маєте:", dollar_number, "$", "Долларів")
