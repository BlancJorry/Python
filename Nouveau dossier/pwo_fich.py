import os
import re

def li_nan_fich():
    try:
        global antre
        antre = input('mete paf fichye a : ')
        if os.path.exists(antre):
            with open(antre, 'r') as e:
                global contenu
                contenu = e.read()
                e.close
            
        else:
            print("Fichier non trouvé.")
    except FileNotFoundError:
        print("Le fichier n'existe pas.")
    except IsADirectoryError:
        print("Le chemin correspond à un répertoire.")
    except PermissionError:
        print("Permission refusée pour accéder au fichier.")

       


def update():
    try:
        mete = input('ekri sa wap met nan fiche a :')
        if os.path.exists(antre):
            with open(antre,'a') as e:
                e.write(mete)
        else:
            print("nou pa jwen fichye sa .")
    except FileNotFoundError:
        print("fichye sa pa existe.")
    except IsADirectoryError:
        print("chemin sa se chemin on repetwa.")
    except PermissionError:
        print("nou pa gen pemisyon poun aksede a fichye sa.")  

def aff():
    if contenu.strip() =="" :
        print('fichye a vid')
    else:
        try:
            print(f"kontni fichye {antre} a se  :")
            print(contenu)   
        except NameError as f:
            print(f)    


def netwaye():
    t = [1,2,3]
    while True:
        print('1.retire espas devant ak deye')
        print('2.retire karakte spesyal yo')
        print('3.soti')
        vle = int(input('antre saw vle fe a :'))
        while vle not in t:
            vle = int(input('tape youn nan nimero opsyon ki devan w yo :'))  

        if vle == 1:
            f = open(antre,'r')
            c = f.read()
            sak_pe_gen_esp = c.strip()
            print('espas yo soti')    
        if vle == 2:
            f = open(antre,'r')
            c = f.read()
            global sans_karakte
            sans_karakte = re.sub(r'[^\w\s]', '', c)
            f.close()
        if vle == 3:
            break 

def sov_teks():
    a = 'C:/Bureau'
    b ='sove.txt'
    c = os.path.join(a,b)
    try:
        k=open(c,'a')
        k.write(sans_karakte)
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)    




while True:
    print("-----------meni-----------")
    print('1. Read Text File')
    print('2. Display Text')
    print('3. Update Text')
    print('4. Clean Text')
    print('5. Save Text')
    print('6. Exit')
    opsyon = [1,2,3,4,5,6]
    try:
        chwa = int(input('antre nimero operasyon ou vle fe a :'))
        while chwa not in opsyon:
            chwa = int(input('saw chwazi a pa nan opsyon yo :'))
    except NameError as p:
        print(p) 
    except ValueError as p:
        print(p)            

    if chwa == 1 :
        li_nan_fich()
    if chwa == 2:
        aff()
    if chwa == 3:
        update()   
    if chwa == 4:
        netwaye()  
    if chwa == 5:
        sov_teks()            
    if chwa == 6:
        print('Goodbye!')
        break       