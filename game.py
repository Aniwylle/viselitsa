from tkinter import *
import random
import json

root = Tk()
root.title("Виселица")
icon = PhotoImage(file="images/icon.png")
root.iconphoto(False, icon)
canvas = Canvas(root, width=600, height=400)
canvas.pack()


def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 29, y + 29, fill="white", outline="blue")
            x = x + 29
        y = y + 29


fag = """Привет! давай поиграем в Виселицу?
Правила ты знаешь. Быстрее жми на кнопку!!"""
canvas.create_text(310, 110, text=fag, fill="purple", font=("helvetica", "19"))


def loading_jsonword():
    with open("slova.json", "r", encoding="utf-8") as file:
        words = json.load(file)
        random.shuffle(words)
        return words


def get_finalword(words):
    word = random.choice(words)
    return word["slova"], word["description"]

def arr():
    but()
    slova, descripstlova = get_finalword(loading_jsonword())
    word = slova
    wo = word
    wor = []
    for i in wo:
        wor.append(i)
    a0 = canvas.create_text(282, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a1 = canvas.create_text(311, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a2 = canvas.create_text(340, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a3 = canvas.create_text(369, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a4 = canvas.create_text(398, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a5 = canvas.create_text(427, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a6 = canvas.create_text(456, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a7 = canvas.create_text(485, 40, text="_", fill="purple", font=("Helvetica", "18"))
    list1 = [0, 1, 2, 3, 4, 5, 6, 7]
    alfabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    er = []
    win = []
    canvas.create_text(410, 100, text=descripstlova, fill="purple", font=("Times New Roman", "15"), )
    def palka():
        canvas.create_line(30, 370, 30, 30, width=4)
        canvas.create_line(150, 30, 30, 30, width=4)
        canvas.create_line(30, 79, 79, 30, width=4)
        canvas.create_line(15, 370, 59, 370, width=4)

    palka()

    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]

        if v in wor:
            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = "1"

            def kord():
                if b2 == 0:
                    x1, y1 = 282, 40
                if b2 == 1:
                    x1, y1 = 311, 40
                if b2 == 2:
                    x1, y1 = 340, 40
                if b2 == 3:
                    x1, y1 = 369, 40
                if b2 == 4:
                    x1, y1 = 398, 40
                if b2 == 5:
                    x1, y1 = 427, 40
                if b2 == 6:
                    x1, y1 = 456, 40
                if b2 == 7:
                    x1, y1 = 485, 40
                return x1, y1

            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(
                x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18")
            )

            btn[key]["bg"] = "green"

            if not v in wor:
                btn[key]["state"] = "disabled"
            if v in wor:
                win.append(v)
                ind2 = wor.index((v))
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(
                    x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18")
                )
            if len(win) == 8:
                canvas.create_text(
                    350,
                    250,
                    text="Ты победил!",
                    fill="purple",
                    font=("Helvetica", "18"),
                )
                for i in alfabet:
                    btn[i]["state"] = "disabled"
        else:
            er.append(v)
            btn[key]["bg"] = "red"
            btn[key]["state"] = "disabled"

            if len(er) == 1:
                golova()
            elif len(er) == 2:
                telo()
            elif len(er) == 3:
                rukaL()
            elif len(er) == 4:
                rukaR()
            elif len(er) == 5:
                nogaL()
            elif len(er) == 6:
                nogaR()
                end()
            root.update()

    btn = {}

    def gen(u, x, y):
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))

    x = 260
    y = 120
    for i in alfabet[0:8]:
        gen(i, x, y)
        x = x + 33
    x = 260
    y = 146
    for i in alfabet[8:16]:
        gen(i, x, y)
        x = x + 33
    x = 260
    y = 172
    for i in alfabet[16:24]:
        gen(i, x, y)
        x = x + 33
    x = 260
    y = 198
    for i in alfabet[24:36]:
        gen(i, x, y)
        x = x + 33

    def golova():
        canvas.create_oval(79, 39, 120, 80, width=4, fill="white")
        canvas.create_line(100, 39, 100, 30, width=4)
        root.update()

    def telo():
        canvas.create_line(100, 80, 100, 200, width=4)
        root.update()

    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4)
        root.update()

    def rukaR():
        canvas.create_line(100, 80, 145, 100, width=4)
        root.update()

    def nogaL():
        canvas.create_line(100, 200, 45, 300, width=4)
        root.update()

    def nogaR():
        canvas.create_line(100, 200, 145, 300, width=4)
        root.update()

    def end():
        canvas.create_text(
            350, 250, text="Ты проиграл!", fill="purple", font=("Helvetica", "18")
        )
        for i in alfabet:
            btn[i]["state"] = "disabled"


btn01 = Button(root, text="Начать!", width=10, height=2, command=lambda: arr())
btn01.place(x=250, y=300)
btn01["bg"] = "#c91010"

root.mainloop()