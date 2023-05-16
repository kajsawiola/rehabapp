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
window.configure(bg="#e4d5b7")

welcome = tk.Label(window, text="Välkommen, Kajsa", font=("Consolas", 20, "italic", "bold"), fg="#800080", bg="#e4d5b7")
welcome.pack(pady=50)
info = tk.Label(window, text="Här har du tillgång till allt som rör ditt besök på sjukgymnastiken. Navigera genom att klicka på de olika knapparna.", font=("Consolas", 14), fg="#800080", bg="#e4d5b7")
info.pack(pady=30)
nyTid = tk.Label(window, text="Du rekommenderas boka en ny tid efter 3 veckors rehabträning.", font=("Consolas", 14), fg="#800080", bg="#e4d5b7")
nyTid.pack(pady= 30)

button_frame = tk.Frame(window)
button_frame.configure(bg="#e4d5b7")


rehab_button = tk.Button(button_frame, text= "Visa träningsprogram", command = open_pdf, width=30, height=10, font=("Verdana", 16, "bold"), bg="#8c92ac", fg="#5b264f" )
boka_button = tk.Button(button_frame, text = "Boka ny tid", command = open_boka, width=30, height=10, font=("Verdana", 16, "bold"), bg="#8c92ac", fg="#5b264f")
diagnos_button = tk.Button(button_frame, text = "Information om mina besvär", command =open_diagnos, width=30, height=10, font=("Verdana", 16, "bold"), bg="#8c92ac", fg="#5b264f")

boka_button.pack(side="left", padx=50, pady=100)
rehab_button.pack(side="left", padx=50, pady=100)
diagnos_button.pack(side="left", padx=50, pady=100)

button_frame.pack()

window.mainloop()