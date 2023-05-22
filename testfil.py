import tkinter as tk
import webbrowser
from tkinter import filedialog

def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        # Koda för att öppna PDF-filen här
        print("Öppnar PDF-filen:", file_path)

def open_link():
    webbrowser.open("https://www.google.com")  # Byt ut länken mot din önskade länk

def show_text():
    text = "Detta är texten som ska visas i programmet."
    print(text)

# Skapa huvudfönstret
window = tk.Tk()

# Skapa knapparna
pdf_button = tk.Button(window, text="Öppna PDF", command=open_pdf)
pdf_button.pack()

link_button = tk.Button(window, text="Öppna länk", command=open_link)
link_button.pack()

text_button = tk.Button(window, text="Visa text", command=show_text)
text_button.pack()

# Starta huvudloopen för att visa fönstret
window.mainloop()
