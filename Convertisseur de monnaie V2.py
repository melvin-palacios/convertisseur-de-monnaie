from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("315x375")
window.resizable(FALSE,FALSE)
onglet = ttk.Notebook(window)
onglet.config(width=315,height= 375)
onglet.pack()
frame1 = Frame(onglet, bg="#2A77EA", width=315, height=375)
frame2 = Frame(onglet, bg="#2A77EA", width=315, height=375)
button_frame = Frame(frame1,bg="#2A77EA")
frame1.pack(expand=1, fill=BOTH)
frame2.pack(expand=1, fill=BOTH)
button_frame.pack()
onglet.add(frame1, text="Conversion")
onglet.add(frame2, text="Historique")


def calcul():
    clear()
    if valeur.get() != "":
        if variable1.get() == "EUR" and variable2.get() == "JPY":
            result = round(float(valeur.get()) / taux_de_change['EUR_JPY'],5)
            valeur2.insert(0, str(result))
            valeur2.place(x=45, y=290)
        elif variable1.get() == "EUR" and variable2.get() == "USD":
            result = round(float(valeur.get()) / taux_de_change['EUR_USD'],5)
            valeur2.insert(0, str(result))
            valeur2.place(x=45, y=290)
        elif variable1.get() == "USD" and variable2.get() == "EUR":
            result = round(float(valeur.get()) / taux_de_change['USD_EUR'],5)
            valeur2.insert(0, str(result))
            valeur2.place(x=45, y=290)
        elif variable1.get() == "USD" and variable2.get() == "JPY":
            result = round(float(valeur.get()) / taux_de_change['USD_JPY'],5)
            valeur2.insert(0, str(result))
            valeur2.place(x=45, y=290)
        elif variable1.get() == "JPY" and variable2.get() == "EUR":
            result = round(float(valeur.get()) / taux_de_change['JYP_EUR'],5)
            valeur2.insert(0, str(result))
            valeur2.place(x=45, y=290)
        elif variable1.get() == "JPY" and variable2.get() == "USD":
            result = round(float(valeur.get()) / taux_de_change['JPY_USD'],5)
            valeur2.insert(0, str(result))
            valeur2.place(x=45, y=290)
        else:
            valeur2.insert(0, "Conversion invalide")
            valeur2.place(x=45, y=290)
    else:
        valeur2.insert(0, "Conversion invalide")
        valeur2.place(x=45, y=290)


def clear():
    valeur2.delete(0, END)


def save():
    global historique
    if variable1.get() == "EUR" and variable2.get() == "JPY":
        historique += f"{valeur.get()}  EUR --> JPY  {valeur2.get()}\n"
    elif variable1.get() == "EUR" and variable2.get() == "USD":
        historique += f"{valeur.get()}  EUR --> USD  {valeur2.get()}\n"
    elif variable1.get() == "USD" and variable2.get() == "EUR":
        historique += f"{valeur.get()}  USD --> EUR  {valeur2.get()}\n"
    elif variable1.get() == "USD" and variable2.get() == "JPY":
        historique += f"{valeur.get()}  USD --> JPY  {valeur2.get()}\n"
    elif variable1.get() == "JPY" and variable2.get() == "EUR":
        historique += f"{valeur.get()}  JPY --> EUR  {valeur2.get()}\n"
    elif variable1.get() == "JPY" and variable2.get() == "USD":
        historique += f"{valeur.get()}  JPY --> USD  {valeur2.get()}\n"
    label_historique.config(text=historique)


historique = ""

taux_de_change = {'EUR_USD': 0.92, 'EUR_JPY': 0.0071,
                  'USD_EUR': 1.08, 'USD_JPY': 0.0077,
                  'JYP_EUR': 140.13, 'JPY_USD': 129.18}

DEVISE1 = [
"          ",
"EUR",
"USD",
"JPY"
]
DEVISE2 = [
"          ",
"EUR",
"USD",
"JPY"
]
# frame 1

label_title = Label(frame1, text="Valeur a convertir", font=("Arial", 15), bg='#2A77EA', fg='White')
label_title.pack(pady=10)

valeur = Entry(frame1,font=("Arial", 15))
valeur.pack(pady=1)

variable1 = StringVar(frame1)
variable1.set(DEVISE1[0])

variable2 = StringVar(frame1)
variable2.set(DEVISE2[0])

menu1 = OptionMenu(frame1, variable1, *DEVISE1)
menu1.pack(pady=10)

menu2 = OptionMenu(frame1, variable2, *DEVISE2)
menu2.pack(pady=1)

convert_button = Button(frame1, text="  convertir  ", font=("Arial",15), bg='white', fg='#2A77EA',command=calcul)
convert_button.place(x=12, y=190)

save_button = Button(frame1, text="  sauvegarder  ", font=("Arial",15), bg='white', fg='#2A77EA',command=save)
save_button.place(x=150,y=190)

label_text1 = Label(frame1, text="Valeur convertie", font=("Arial",15), bg='#2A77EA',fg='White')
label_text1.place(x=87.5, y=255)

valeur2 = Entry(frame1,font=("Arial", 15))
valeur2.place(x=45, y=290)

# frame 2
label_title_historique = Label(frame2,text="Historique", font=("Arial",20), bg='#2A77EA',fg='White')
label_title_historique.pack(pady=10)

label_historique = Label(frame2,bg="#2A77EA",fg="white",font=("Arial", 14))
label_historique.pack()

window.mainloop()
