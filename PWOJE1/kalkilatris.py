

kantite_not = int(input('antre kantite not ou vle kalkile moyen ou an :'))
    
lis_not = []
for i in range(0,kantite_not):
    note = int(input('entre note no ' +str(i+1)+ ' svp:'))
    while note > 100:   # tes ki pou fe moun nan paka antre not yo pi gro ke 100
        note = int(input(' note ou yo dwe sou baz 100 re antre not sa :'))
    lis_not.append(note)
print("not ou yo se :",lis_not)
s = sum(lis_not)
M = s/kantite_not

if(M>=90):
    print('moyen ou c:'+str(M)+ ' A')
if(M>=80 and M<90):
    print('moyen ou c:'+str(M)+ ' B')    
if(M>=70 and M<80):
    print('moyen ou c:'+str(M)+ ' C')   
if(M>=60 and M<70):
    print('moyen ou c:'+str(M)+ ' D')   
if( M<60):
    print('moyen ou c:'+str(M)+ ' F')