import colorama
from colorama import Fore, Back, Style



random_class = input("Виберіть один з трьох класів (Back, Fore, Style): ")

if random_class == ("Fore"):
    print("Клас Fore використовують для зміни кольору тексту:")
    print(Fore.RED + "Червоний текст")

elif random_class == ("Back"):
    print("Клас Back використовують для зміни заднього фону тексту:")
    print(Back.RED + "Текст на червоному фоні")

elif random_class == ("Style"):
    print("Клас Style використовують для зміни стилю тексту:")
    print(Style.NORMAL + "Нормальний текст")
    print(Style.BRIGHT + "Жирний текст")

else:
    for method in dir(colorama):
        print(method)