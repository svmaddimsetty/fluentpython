ships = ["NY","CH","IN","OH"]
cargos = ["Land","water","sky"]
x = ((a,b) for a in ships for b in cargos)
print(x)

symbols = "$%^&*#()*%#"
asc = tuple((ord(sym) for sym in symbols))

print(asc)

import array
l=array.array("I",(ord(each) for each in symbols))

print(l)

def sum_num(x,*list):
    return sum(list)

a=sum_num(1,2,3)
#print(a)

b=sum_num(1,2,3,4)
#print(b)

def generator(): 
    t = 1
    print ('First result is ',t) 
    yield t 
 
    t += 1
    print ('Second result is ',t) 
    yield t 
 
    t += 1
    print('Third result is ',t) 
    yield t 

x = generator()


for each in x:
    print("loop starts:",each)
    next(x)
    print("loop ends:",each)























