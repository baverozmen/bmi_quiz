from tkinter import *

window = Tk()

window.minsize(width=300, height=200)

lab1 = Label(text="kilonuzu giriniz(kg)")
lab1.config(fg="black")

lab1.pack()


ent1 = Entry(width=30)
ent1.pack()

lab2 = Label(text="boyunuzu girin(cm):")
lab2.config(fg="black")
lab2.pack()

ent2 = Entry(width=30)
ent2.pack()

global sonuc

def bmi():
    global sonuc
    x = int(ent1.get())
    y = int(ent2.get())
    sonuc = x / ((y/100) ** 2)

    x = round(sonuc)

    if x < 18.5:
        Label(text=f"aşırı zayıf: {x}").pack()

    elif 18.5 <x < 24.5:
        lab4 = Label(text=f"normal: {x}")
        lab4.pack()

    elif 24.5 <= x < 29.5:
        lab5 = Label(text=f"şişman: {x}")
        lab5.pack()
    elif 29.5 <= x <34.9:
        lab6 = Label(text=f"obez: {x}")
        lab6.pack()
    elif 34.9 <= x:
        lab7 = Label(text=f"aşırı obez: {x}")
        lab7.pack()
    else:
        lab8 = Label(text="degerleri dogru giriniz")
        lab8.pack()





bttn = Button(text="bmı test", command=bmi)
bttn.pack()





window.mainloop()