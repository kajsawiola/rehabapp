#rehabappen
import tkinter as tk

window = tk.Tk()

welcome = tk.Label(window, text="Välkommen, Kajsa")
info = tk.Label(window, text="Här har du tillgång till allt som rör ditt besök på sjukgymnastiken. Navigera genom att klicka på de olika knapparna.")
nyTid = tk.Label(window, text="Du rekommenderas boka en ny tid efter 3 veckors rehabträning.")
welcome.pack()
info.pack()
nyTid.pack()

window.mainloop()