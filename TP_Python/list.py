#1
lis2 = []
for i in range(0,18):
    if i%2 == 0:
        lis2.append(i)
print(lis2)

#2
lisch = [1,2,3,4,5,6,7,8,9]
lisch = str(lisch)
print(lisch)

#3
mini =["a","b","c","d","e"]
for el in range(len(mini)):
    mini[el] = mini[el].upper()
print(mini)    

#4
lisd = [0,1,2,3,4,5,6,7,8,9,10]
lisd3=[]
for el in range(len(lisd)):
    if lisd.index(el)%3 == 0:
        lisd3.append(el)
print(lisd3)

#5
lisel = [1, 2, 3, 4, 5, 6, 7, 8, 90, 0, 23, 45, 76]
listip = []

temp_tuple = []

for el in lisel:
    temp_tuple.append(el)
    
    if len(temp_tuple) == 3:
        listip.append(tuple(temp_tuple))
        temp_tuple = [] 

if temp_tuple:
    listip.append(tuple(temp_tuple))

print(listip)

#6
liselrep = [2,4,4,5,8,8,8,9,2,1,0]
j=1
for i in liselrep:
    if liselrep.count(i)>1:
        liselrep.remove(i)
print(liselrep)      

#7
l1 =[1,3,6,8,0,3,5]
l2=[1,5,7,8]
l3=[]
for i in l1:
    for j in l2:
        if j == i:
            l3.append(i)
print(l3)

#8
l4=[]# poko fini
for i in l1:
    for j in l2:
        if j !=i:
            l4.append(j)
print(l4)  

#9
