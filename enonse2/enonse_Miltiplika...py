
n = True
repons_n = 'n'
repons_p = 'w'
while n:
    nonb_itilizate_a = int(input('entrer yon nonb :'))
    for i in range(1,11):
        print(nonb_itilizate_a, 'X', i, '=', nonb_itilizate_a*i)
    repons = input('ou vle rekomanse ? tape (w) pou wi ou byen (n) pou non')
    if(repons == repons_n):
        print('mesi')
        break
    if(repons == repons_p):
        continue
    if(repons != repons_p and repons != repons_n):
        while n:
            repons = input('ou dwe tape (w) pou wi ou byen (n) pou non')
            if(repons == repons_n or repons == repons_p):
                break
    
    if(repons == repons_n):
        print('mesi')
        break
        
    
                       
                       
