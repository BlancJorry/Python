import tkinter as tk

def evaluer():
    try:
        expression = entry.get()
        resultat = eval(expression)
        label_resultat.config(text="Résultat : " + str(resultat))
    except Exception as e:
        label_resultat.config(text="Erreur")

fent = tk.Tk()
fent.title("Calculatrice")
fent.geometry('600x350')


entry = tk.Entry(fent,width=30)
entry.grid(row=0, column=0, columnspan=4)



label_resultat = tk.Label(fent, text="")
label_resultat.grid(row=1, column=0, columnspan=4)



boutons = [
    ('7', 'beige'),
    ('8', 'beige'),
    ('9', 'beige'),
    ('/', 'green'),
    ('4', 'beige'),
    ('5', 'beige'),
    ('6', 'beige'),
    ('*', 'orange'),
    ('1', 'beige'),
    ('2', 'beige'),
    ('3', 'beige'),
    ('-', 'red'),
    ('0', 'beige'),
    ('.', 'beige'),
    ('=', 'beige'),
    ('+', 'yellow')
]


ligne = 2
colonne = 0
dis =4


for bt,couleur in boutons:
    
    if bt == '=':
        tk.Button(fent, text=bt, width=2, height=0, bg=couleur,font=('Helvetica',20,'bold'), command=evaluer).grid(row=ligne, column=colonne)
    else:
        tk.Button(fent, text=bt, width=2, height=0,bg=couleur ,font=('Helvetica',20,'bold'),command=lambda b=bt: entry.insert(tk.END, b)).grid(row=ligne, column=colonne,padx=dis,pady=dis )
    
    colonne += 1
    if colonne > 3:
        colonne = 0
        ligne += 1

fent.mainloop()
