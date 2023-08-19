from products import af_pwo,pwodwi
from cart import ajoute,panye,af_panye_som

def meni():
    vre = True

    while vre:
        print("----------Bonjou byenvini nan boutik JB-----------")
        print('1.Chache pwodwi')
        print('2.Wè panye ak tout pri total')
        print("3.Fèmen")
        try:
            chwa = int(input("fe yon chwa :"))

            if chwa == 1:
                af_pwo(pwodwi)
                ajoute(pwodwi,panye) 
            if chwa == 2:
                af_panye_som(panye)     
            if chwa == 3:
                print('mesi')
                break    
        except ValueError:
            print('chwa ou a pa nan meni an!')        
   
meni()    
