#rehabappen
import tkinter as tk
import webbrowser
from tkinter import ttk

def open_pdf():
    rehabProgram = r"C:\Users\Användar\PycharmProjects\pythonProject2\projketarbete maj23\Kajsa.pdf"
    webbrowser.open(rehabProgram)

def open_boka():
    webbrowser.open("https://e-tjanster.1177.se/mvk/login/login.xhtml")

def open_diagnos():
    webbrowser.open("https://www.1177.se/Orebrolan/sjukdomar--besvar/skelett-leder-och-muskler/leder/artros---ledsvikt/")

window = tk.Tk()

welcome = tk.Label(window, text="Välkommen, Kajsa")
welcome.pack()
info = tk.Label(window, text="Här har du tillgång till allt som rör ditt besök på sjukgymnastiken. Navigera genom att klicka på de olika knapparna.")
info.pack()
nyTid = tk.Label(window, text="Du rekommenderas boka en ny tid efter 3 veckors rehabträning.")
nyTid.pack()

button_frame = ttk.Frame(window)

rehab_button = ttk.Button(button_frame, text= "Visa träningsprogram", command = open_pdf)
boka_button = ttk.Button(button_frame, text = "Boka ny tid", command = open_boka)
diagnos_button = ttk.Button(button_frame, text = "Information om mina besvär", command =open_diagnos )

boka_button.pack(side="left", padx=5, pady=5)
rehab_button.pack(side="left", padx=5, pady=5)
diagnos_button.pack(side="left", padx=5, pady=5)

button_frame.pack()

window.mainloop()