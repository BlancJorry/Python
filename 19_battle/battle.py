
lis = [1,2,3,4,5]

def pg (l):
    t = l[0]
    for i in l:
       if i > t:
           t=i
    print('pigran c',t)    
pg(lis)    


def pt (l):
    t = l[0]
    for i in l:
       if i < t:
           t=i
    print('pigran c',t) 
pt(lis)    
