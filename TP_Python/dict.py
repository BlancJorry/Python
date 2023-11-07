#1
a ={"nom":"Blanc","prenom":"Jorry","age":23}
b=[]
for i ,v in a.items():
    b.append(v)
print(b)

#2
antre = input("antre on vale:")
for el in antre:
    if el[0] == "{" and antre[-1] == "}":
        print('gen akolad')
        break
    else:
        print("pa gen akolad")
        break    

#3
for el in a:
    print(el)

#4
for e,a in a.items():
    print(a)    

#5
dica = {"a":1,"b":2,"c":3,"d":4}
dicb={}
for da , db in dica.items():
    pass#poko fini

#6
original_dict = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
mod_dict = {}
for k, v in original_dict.items():
    if isinstance(v, str):
        mod_dict[k] = "_" + v + "_"
    else:
        mod_dict[k] = v
print(mod_dict)

#7
dicun =  {"a": "12", "b": "abc", "c": "12r", "d": "90"}
dicnum={}
for ke,val in dicun.items():
    try:
        valst=int(val)
        dicnum[ke] = valst
    except ValueError as e:
        print(e)    
print(dicnum) 

#8
listtuple = [("a",1), ("b",2)]
dic = {c:vale for c, vale in listtuple}

#9
dictionnaire = {"a": 1, "b": 2}

lis_tip = [(cle, vale) for cle, vale in dictionnaire.items()]

print(lis_tip)

#10

