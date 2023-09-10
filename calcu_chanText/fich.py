import tkinter as tk
from tkinter import filedialog

def operasyon():
    tèks = zone_tèks.get("1.0", "end-1c")
    non_fich = champ_non_fichye.get()

    if tèks.strip() == "" or non_fich.strip() == "":
        print("Erè: Tèks la oswa non fichye a vid.")
    else:
        with open(non_fich + ".txt", "a") as fichye:
            fichye.write(tèks)
        print("Fichye enregistre avèk siksè: " + non_fich + ".txt")

fenet = tk.Tk()
fenet.title("Editè Tèks")
fenet.configure(bg="gray")
fenet.geometry('600x350')

zone_tèks = tk.Text(fenet, height=15, width=45)
zone_tèks.pack(padx=20, pady=10)


frame = tk.Frame(fenet, bg="gray")
frame.pack()

champ_non_fichye = tk.Entry(frame)
champ_non_fichye.pack(side="left")
champ_non_fichye.insert(0,'Nom fichye')

bouton_enregistre = tk.Button(frame, text="Anrejistre", command=operasyon, bg="green",fg="white")
bouton_enregistre.pack(padx=10, pady=10)

fenet.mainloop()