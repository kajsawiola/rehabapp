#rehabappen
import tkinter as tk

window = tk.Tk()

welcome = tk.Label(window, text="Välkommen, Kajsa")
info = tk.Label(window, text="Här har du tillgång till allt som rör ditt besök på sjukgymnastiken. Navigera genom att klicka på de olika knapparna.")
nyTid = tk.Label(window, text="Du rekommenderas boka en ny tid efter 3 veckors rehabträning.")
welcome.pack()
info.pack()
nyTid.pack()

rehab_button = tk.Button(window, text= "Visa träningsprogram")
link_button = tk.Button(window, text = "Boka ny tid")
diagnos_button = tk.Button(window, text = "Information om mina besvär")

rehab_button.pack()
link_button.pack()
diagnos_button.pack()

window.mainloop()