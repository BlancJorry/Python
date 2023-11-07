#1
a = "MWEN se yon bon mouN"
a=a.lower()
print(a)

#2
b = "mwen gen on bon refij"
b = b.split(' ')
print(b)

#3
c = "Mwen gen on bon Refij"
c=c.title()
print(c)

#4
d = "mwen gen on bon refij" #poko fini
d=d.split()
for el in d:
    for i in el:
        n = "".join(el[0])
print(n)

#5
e = "Papa m gen anpil kay"
e=e.replace('a','@')
print(e)    

#6
f= "Ayiti"
f="".join(reversed(f))
g =f.lower()
print(g)


#7
h = "Ayiti bel anpil anpil"
comp =0
for el in h:
    comp +=1
    if el == 'a':
        break
print(comp)  

#8
i = "Ayiti kapab Avanse" 
si = 0
for idi,carac in enumerate(i):
    if carac.lower() =="a":
        si +=idi
print(si)        
        


#9
j = "Ayiti se on bel anti a"# poko fini
indexj =[]
for el,ds in enumerate(j):
    if ds == "a":
        indexj.append(el)
print(indexj)        

#10
j = "Ayiti se on bel anti a"
supesp = j.replace(" ","")
print(supesp)