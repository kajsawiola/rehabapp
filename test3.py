import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
import json

class Person:
    def __init__(self, namn, text, program, diagnos):
        self.namn = namn
        self.text = text
        self.program = program
        self.diagnos = diagnos

    def to_dict(self):
        return {
            'namn': self.namn,
            'text': self.text,
            'program': self.program,
            'diagnos': self.diagnos
        }

    
    def load_from_json(filename="lista.json"):
        persons = []
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                person = Person(item['namn'], item['text'], item['program'], item['diagnos'])
                persons.append(person)
        return persons

def load_person_info(name, persons):
    for person in persons:
        if person.namn == name:
            return person
    return None

def start_program():
    name = name_entry.get()
    person = load_person_info(name, persons)
    if person is None:
        print("Personen finns inte i databasen")
        return
    welcome.config(text=f"Välkommen, {person.namn}")
    rehab_button.config(command=lambda: webbrowser.open(r"C:\Users\Användar\PycharmProjects\pythonProject2\projketarbete maj23\\"+person.program+".pdf"))
    diagnos_button.config(command=lambda: webbrowser.open(person.diagnos))

def open_pdf():
    rehabProgram = r"C:\Users\Användar\PycharmProjects\pythonProject2\projketarbete maj23\Rehab.pdf"
    webbrowser.open(rehabProgram)

def open_boka():
    webbrowser.open("https://e-tjanster.1177.se/mvk/login/login.xhtml")

def open_diagnos():
    webbrowser.open("https://www.1177.se/Orebrolan/sjukdomar--besvar/skelett-leder-och-muskler/leder/artros---ledsvikt/")

persons = Person.load_from_json()

window = tk.Tk()
window.configure(bg="#e4d5b7")

welcome = tk.Label(window, text="Välkommen, ", font=("Consolas", 40, "italic", "bold"), fg="#800080", bg="#e4d5b7")
welcome.pack(pady=20)

info = tk.Label(window, text="Här har du tillgång till allt som rör ditt besök på sjukgymnastiken.\n Navigera genom att klicka på de olika knapparna.", font=("Consolas", 14), fg="#800080", bg="#e4d5b7")
info.pack(pady=15)

nyTid = tk.Label(window, text="Du rekommenderas boka en ny tid efter 3 veckors rehabträning.", font=("Consolas", 14), fg="#800080", bg="#e4d5b7")
nyTid.pack(pady=15)

button_frame = tk.Frame(window)
button_frame.configure(bg="#e4d5b7")

rehab_button = tk.Button(button_frame, text="Visa träningsprogram", command=open_pdf, width=25, height=5, font=("Verdana", 16, "bold"), bg="#8c92ac", fg="#5b264f")
boka_button = tk.Button(button_frame, text="Boka ny tid", command=open_boka, width=25, height=5, font=("Verdana", 16, "bold"), bg="#8c92ac", fg="#5b264f")
diagnos_button = tk.Button(button_frame, text="Information om mina besvär", command=open_diagnos, width=25, height=5, font=("Verdana", 16, "bold"), bg="#8c92ac", fg="#5b264f")

boka_button.pack(side="left", padx=20, pady=20)
rehab_button.pack(side="left", padx=20, pady=20)
diagnos_button.pack(side="left", padx=20, pady=20)

button_frame.pack()

image = Image.open("blomma.jpg")
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)

image_frame = tk.Frame(window)
image_frame.pack(pady=30)

for i in range(4):
    image_label = tk.Label(image_frame, image=photo)
    image_label.grid(row=0, column=i)

name_entry = tk.Entry(window, font=("Consolas", 16))
name_entry.pack(pady=10)

start_button = tk.Button(window, text="Starta program", command=start_program, width=15, height=2, font=("Verdana", 14, "bold"), bg="#8c92ac", fg="#5b264f")
start_button.pack(pady=10)

window.mainloop()