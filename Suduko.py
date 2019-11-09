# Suduko-solving-program
import numpy

def probable_numbers():
    for a in range(0,9):
        for b in range(0,9):
            if suduko[a,b]=='':
                square=block(a,b,'y',suduko)
                for c in [1,2,3,4,5,6,7,8,9]:
                    if str(c) not in suduko[a,:] and str(c) not in suduko[:,b] and str(c) not in square:
                        x[a,b]+=str(c)
    return x
                 
def block(x,y,c,the_array):
    d=[]
    if x==0 or x==1 or x==2:
        if y==0 or y==1 or y==2:
            l=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        elif y==3 or y==4 or y==5:
            l=[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
        elif y==6 or y==7 or y==8:
            l=[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]
    elif x==3 or x==4 or x==5:
        if y==0 or y==1 or y==2:
            l=[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]
        elif y==3 or y==4 or y==5:
            l=[(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]
        elif y==6 or y==7 or y==8:
            l=[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]
    elif x==6 or x==7 or x==8:
        if y==0 or y==1 or y==2:
            l=[(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]
        if y==3 or y==4 or y==5:
            l=[(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]
        elif y==6 or y==7 or y==8:
            l=[(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]
    for e in l:
        d.append(str(the_array[e]))
    if c=='y':
        return d
    if c=='n':
        return l

def pop_from_list(a,b):
    c=list(a)
    c.remove(b)
    return ''.join(c)
           

                   
def row():
    for o in range(0,9):
        d=[]
        for p in range(0,9):
            if len(x[o,p])==1:
                d.append(x[o,p])
        for t in range(0,9):  
            if len(x[o,t])!=1:
                for g in d:
                    if g in x[o,t]:
                        x[o,t]=pop_from_list(x[o,t],g)
                if len(x[o,t])==1:
                    d.append(x[o,t])
def column():                
    for o in range(0,9):
        d=[]
        for p in range(0,9):
            if len(x[p,o])==1:
                d.append(x[p,o])
        for t in range(0,9):  
            if len(x[t,o])!=1:
                for g in d:
                    if g in x[t,o]:
                        x[t,o]=pop_from_list(x[t,o],g)
                if len(x[t,o])==1:
                    d.append(x[t,o])

def box():
    j=[(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
    for variable in j:
        g=[]
        list1=block(variable[0],variable[1],'y',x)
        list2=block(variable[0],variable[1],'n',x)
        for h in list1:
            if len(h)==1:
                g.append(h)
        for y in list1:
            variable2=y
            if len(variable2)!=1:
                for f in g:
                    if f in variable2:
                        variable2=pop_from_list(variable2,f)
                x[list2[list1.index(y)]]=variable2
            
       
line1=['','','','8','','','','','']
line2=['4','','','','1','5','','3','']
line3=['','2','9','','4','','5','1','8']
line4=['','4','','','','','1','2','']
line5=['','','','6','','2','','','']
line6=['','3','2','','','','','9','']
line7=['6','9','3','','5','','8','7','']
line8=['','5','','4','8','','','','1']
line9=['','','','','','3','','','']

suduko=numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])
x=numpy.copy(suduko)
x=x.astype('<U10') 
probable_numbers()
    
for i in range(10):
    row()
    column()
    box()
    
print(x)
    

