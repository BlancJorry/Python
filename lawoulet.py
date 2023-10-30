from random import randrange
import pickle
import os

kanpe = "K"
a = False
def itil(epsedo):
    return ' ' not in epsedo and epsedo.islower()

def main():
    epsedo = input("antre on nom :")
    while True:
        if itil(epsedo):
            break
        else:
            print("pa sipoze gen espas nan nom an e li sipoze miniskil!!!")
            epsedo = input("antre on nom pou komanse:")

            
    chemin = os.path.expanduser("~/Documents")
    non_fich = 'sko.txt'
    non_comp = os.path.join(chemin, non_fich)
    
    global scores
    scores = {}
    score_itil=0

    if os.path.exists(non_comp):
        fich = open(non_comp, "rb")
        scores = pickle.load(fich)
        fich.close()
        if epsedo in scores:
            score_itil = scores[epsedo]
            print(f"Ou te deja jwe denye skò se : {score_itil}. Kontinye jwet ou.")
        else:
            print("Ou se yon nouvo jwè. Kòmanse avèk yon skò 0.")
    else:
        print("Ou se yon nouvo jwèt. skow se 0.")

    
    while True:
        
        nomb_Odi = randrange(0,100)
        print(nomb_Odi)
        chans = 0
        s = 30
        c=5
        while True:
            try:
                vale_Itil = int(input("entrer yon vale :"))#kontrent sou vale itilizate a pral gen poul antre a
                while vale_Itil < 0 or vale_Itil > 100:
                    vale_Itil = int(input("vale ou antre a pa nan inteval [0,100] re antre anko nou pa konte pati sa!:"))
            except ValueError:
                print("saw antre a pa antier")
            except TypeError as e:
                print(e)    

            chans += 1
            s=30
            c-=1
            if nomb_Odi == vale_Itil:
                print(f'ou genyen nonb ou a egal ak nonb machin nan kisa {nomb_Odi}')
                s = s*chans
                score_itil = scores.get(epsedo, 0) + s
                break
            if chans > 4 :
                print('ou pedi, ou pa ret chans anko')
                break    
            if vale_Itil < nomb_Odi:
                print('mete sou nonb ou a li trop piti ou rete ',c,' chans')
            else:
                print('retire sou nonb ou a li trop gro ou ret',c,' chans')  
    
        stop = input("pou kanpe tape k sinon tape on lot karakte :")
        if stop.upper() == kanpe:
            scores[epsedo] = score_itil
            fich = open(non_comp, "wb")
            pickle.dump(scores,fich)
            fich.close()
            break
        else:
            continue    


    print("Jwèt la fini. Sko final ou se:")
    print(epsedo,':',score_itil) 
    scores[epsedo] = score_itil
main() 