from tkinter import *
from tkinter import messagebox
import pickle

def registration():
    b_reg.config(bg = "#66a366")
    b_enter.config(bg ="DarkSeaGreen")
    frame = Frame(root, bg = "PeachPuff")
    frame.place(relwidth = 0.7, relheight = 0.7, relx = 0.15, rely = 0.15)

    label_login = Label(frame, text = "Логин: ", font=16, bg = "PeachPuff")
    label_login.place(relx = 0.1, rely = 0.1)

    label_possword = Label(frame, text = "Пароль: ", font=16, bg = "PeachPuff")
    label_possword.place(relx = 0.1, rely = 0.3)

    label_possword3 = Label(frame, text = "Повторите пароль: ", font=16, bg = "PeachPuff")
    label_possword3.place(relx = 0.1, rely = 0.5)

    entry_login = Entry(frame)
    entry_login.place(relx = 0.5, rely = 0.1, relwidth = 0.4)

    entry_possword = Entry(frame, show = "*")
    entry_possword.place(relx = 0.5, rely = 0.3, relwidth = 0.4)

    entry_possword2 = Entry(frame, show = "*")
    entry_possword2.place(relx = 0.5, rely = 0.5, relwidth = 0.4)

    button_OK = Button(frame, text = "Зарегаться", bg = "White", command = lambda:sign_up())
    button_OK.place(relheight = 0.2, relwidth = 0.4, relx = 0.3, rely = 0.7)


    def sign_up():
        if len(entry_login.get()) < 6:
            messagebox.showerror("Ошибка!", "Логин слишком короткий")
            entry_login.config(bg = "red")
        elif len(entry_possword.get()) < 6:
            messagebox.showerror("Ошибка!", "Пароль слишком короткий")
            entry_possword.config(bg = "red")
        elif entry_possword.get() != entry_possword2.get():
            messagebox.showerror("Ошибка!", "Пароли не совпадаит.")
            entry_possword2.config(bg = "red")
        else:
            save()
    def save():
        data = dict()
        data[entry_login.get()] = entry_possword.get()
        f = open("user.txt", "wb")
        import pickle
        pickle.dump(data, f)
        messagebox.showinfo("Успех!", f"Новый пользователь {entry_login.get()} зарегестрирован!")

def login_from():
    b_reg.config(bg = "DarkSeaGreen")
    b_enter.config(bg ="#66a366")

    frame = Frame(root, bg = "PeachPuff")
    frame.place(relwidth = 0.7, relheight = 0.7, relx = 0.15, rely = 0.15)

    label_login = Label(frame, text = "Логин: ", font=16, bg = "PeachPuff")
    label_login.place(relx = 0.1, rely = 0.1)

    label_possword = Label(frame, text = "Пароль: ", font=16, bg = "PeachPuff")
    label_possword.place(relx = 0.1, rely = 0.3)

    entry_login = Entry(frame)
    entry_login.place(relx = 0.5, rely = 0.1, relwidth = 0.4)

    entry_possword = Entry(frame, show = "*")
    entry_possword.place(relx = 0.5, rely = 0.3, relwidth = 0.4)

    button_OK = Button(frame, text = "Войти", bg = "White", command = lambda:login_pass())
    button_OK.place(relheight = 0.2, relwidth = 0.4, relx = 0.3, rely = 0.7)

    def login_pass():
        f = open("user.txt", "rb")
        data = pickle.load(f)
        f.close()
        if entry_login.get() in data and entry_possword.get() == data[entry_login.get()]:
            messagebox.showinfo("Успех!", "Вы вошли в приложение!")
        else:
            messagebox.showerror("Ошибка!", "Неправильный логин или пароль")

root = Tk()
root.title("Форма для фхода")
root.geometry("550x550")
root.resizable(False, False)

root.config(bg = "HoneyDew")

img = PhotoImage(file = "bg.gif")
label_bg = Label(root, image = img)
label_bg.place(relheight = 1, relwidth = 1)

b_reg = Button(root, text ="Зарегестрироваться", bg ="DarkSeaGreen", fg ="DarkOliveGreen", command = registration)
b_reg.place(relx = 0.2, rely = 0.1, relwidth = 0.3)

b_enter = Button(root, text="Войти", bg="DarkSeaGreen", fg="DarkOliveGreen", command = login_from)
b_enter.place(relx = 0.5, rely = 0.1, relwidth = 0.3)


root.mainloop()
