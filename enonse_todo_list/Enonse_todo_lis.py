import pickle
import os
Todo_list = []

def add_task():
    O="o"
    N="n"
    n= True
    while n :
        des = input("antre deskripsyon yon tach :")
        Todo_list.append(des)
        repons = input('ou vle kontinye ?')
        if(repons == N):
            break    
        if(repons == O):
            continue
        if(repons != N and repons != O):
            while n:
                repons = input('ou dwe tape (o) pou wi ou byen (n) pou non')
                if(repons == O or repons == N):
                    break
        if(repons == N):
            break        

def display_tasks(l):
    n=0
    print("lis tach ou yo se :")
    for i in Todo_list:
        n+=1
        print(n,'-',i)


def mark_task_done():
    try:
        fini = int(input('antre nimero tach ki fini an '))
        n=fini-1
        Todo_list.pop(n)
    except IndexError:
        print('antre yon nimero korek')    
    print('tach nimero {} la fini li soti nan lis la '.format(fini))        


def save_tasks(l):
    chemin_dos ="C:/Users/Blanc/Documents/cours PYTHON"
    non_fich = 'task.txt'
    non_comp = os.path.join(chemin_dos, non_fich)
    try:
        fich = open(non_comp,'rb')
        for t in Todo_list:
            pickle.dump(l,fich)
            l= pickle.load(fich)
            print('fichye ou yo anregistre')   
    except OSError as e:
        print('gen ere nan anregistreman !!!',str(e))    
    fich.close()


def meni():
    vre = True
    while vre :
        print('/-------------------Meni---------------/')
        print('chwazi operasyon ou vle fe a')
        print('1.Ajoute tach')
        print('2.Afiche tach yo')
        print('3.fini yon tach tach')
        print('4.Anregistre epi femen')
        chwa = int(input("fe yon chwa :"))

       try:
            chwa = int(input("fe yon chwa :"))

            if chwa == 1:
                add_task()
            if chwa == 2:
                display_tasks(Todo_list)
            if chwa == 3:
                mark_task_done()
            if chwa == 4:
                save_tasks(Todo_list)
                print('eleman ou yo anregistre nan fichye a !')
            if chwa == 0:
                print('program nan femen mesi')
                break
        except ValueError:
            print('chwa ou a pa nan meni an')
meni()
