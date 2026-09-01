from Gorbe import *
import tkinter as tk

def catgui():
    global panjere
    panjere = tk.Tk()
    panjere.title("Vitural Cat")
    panjere.geometry("400x300")
    matn = tk.Label(panjere,text = "اسم گربه ت دوست داری چی باشه؟")
    matn.pack()
    vorudi1 = tk.Entry(panjere)
    vorudi1.pack()
    def click1():
        global dokme2,dokme3,dokme4,dokme5,dokme6,dokme7,cat,matn2
        cat = VirtualCat(f"{vorudi1.get()}")
        vorudi1.pack_forget()
        matn.config(text = "حالا میخوای چیکار کنی؟")
        matn2 = tk.Label(panjere,text = f"{cat.status()}")
        matn2.pack()
        dokme2 = tk.Button(panjere,text = "Feed",command = feed_action)
        dokme3 = tk.Button(panjere,text = "Play",command = play_action)
        dokme4 = tk.Button(panjere,text = "Sleep",command = sleep_action)
        dokme5 = tk.Button(panjere,text = "Tick",command = tick_action)
        dokme6 = tk.Button(panjere,text = "Auto_pilot",command = auto_pilot_action)
        dokme7 = tk.Button(panjere,text = "Mew",command = mew_action)
        dokme2.pack()
        dokme3.pack()
        dokme4.pack()
        dokme5.pack()
        dokme6.pack()
        dokme7.pack()
        vorudi1.pack_forget()
        dokme1.pack_forget()
        panjere.geometry("400x600")

    def feed_action():
        matn3 = tk.Label(panjere,text =f"{cat.feed()}")
        matn3.pack()
        matn2.config(text=cat.status())
    def play_action():
        matn4 = tk.Label(panjere,text =f"{cat.play()}")
        matn4.pack()
        matn2.config(text=cat.status())
    def sleep_action():
        matn5 = tk.Label(panjere,text =f"{cat.sleep()}") 
        matn5.pack()
        matn2.config(text=cat.status())
    def tick_action():
        matn6 = tk.Label(panjere,text =cat.status())
        matn6.pack()
        matn2.config(text=cat.status())
    def auto_pilot_action():
        matn7 = tk.Label(panjere,text = cat.status())
        matn7.pack()
        matn2.config(text=cat.status())
    def mew_action():
        matn8 = tk.Label(panjere,text = f"{cat.mew()}")
        matn8.pack()
        matn2.config(text=cat.status())

    dokme1 = tk.Button(panjere,text = "confirm",command = click1)
    dokme1.pack()
    name = vorudi1.get()
    if name.isalpha() == True:
        pass
    else:
        print("invalid name!")
    panjere.mainloop()

catgui()