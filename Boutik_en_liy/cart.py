
panye = []

def ajoute(pwodwi,panye):
    e=0
    n=1
    while n >0 :
      num = int(input("antre numero pwodwi ou vle mete nan panye ou a :"))
      kantite = int(input('antre ki kantite ou vle nan pwodwi sa:'))
      if 1 <= num <= len(pwodwi):
        panye.append(pwodwi[num-1])
        panye[e]['Quantite'] = kantite
        e+=1
      try:  
        anko = int(input('ou vle mete nan panye ou a anko ? peze 0 si non nenpot lot chif pou oui!'))  
        if anko == 0:
          break 
        else:
          continue 
      except ValueError:
         anko = int(input('peze chif :')) 


def af_panye_som(p):
    print('-----panye ou gen pwodwi sa yo-----')
    s=0
    for el in p:
       print(el)
    ''' for y in p:   
       s = s + p[y]['price']*['Quantite']
    print(s) '''  
    
  

