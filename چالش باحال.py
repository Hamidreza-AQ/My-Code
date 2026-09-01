import tkinter as tk

panjere = tk.Tk()
panjere.title("چالش باحال")
panjere.geometry("250x300")

matn = tk.Label(panjere,text = "اسمت چیه؟")
matn.pack()

vorudi = tk.Entry(panjere)
vorudi.pack()

dokme2 = None
dokme3 = None
def click1():
    global dokme2,dokme3
    name = vorudi.get()
    matn.config(text = f" {name} دوسم داری؟")
    dokme1.pack_forget()
    dokme2 = tk.Button(panjere,text = "نه",command = click2)
    dokme3 = tk.Button(panjere,text = "آره",command = click3)
    dokme2.pack()
    dokme3.pack()
dokme1 = tk.Button(panjere,text = "ثبت",command = click1)
dokme1.pack()

def click2():
    name = vorudi.get()
    matn.config(text = f"اشکالی نداره {name} ممنون که نظرت رو گفتی")
    dokme2.pack_forget()
    dokme3.pack_forget()
    vorudi.pack_forget()
def click3():
    name = vorudi.get()
    matn.config(text = f"❤️منم دوست دارم {name}")
    dokme2.pack_forget()
    dokme3.pack_forget()
    vorudi.pack_forget()

panjere.mainloop()