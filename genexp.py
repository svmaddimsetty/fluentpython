ships = ["NY","CH","IN","OH"]
cargos = ["Land","water","sky"]
x = ((a,b) for a in ships for b in cargos)
print(x)

symbols = "$%^&*#()*%#"
asc = tuple((ord(sym) for sym in symbols))

print(type(asc))

name, age, color = ('Swamy',15,"Black")
k = ('Swamy',15,"Black")

print(type(name))
print(type(k))



y = [1,7,8,9]

for each in y:
    print(each)

def gree():
    print("hi how are you")

l = gree()

print(type(l))


def gene(): 
    t = 1
    print ('First result is ',t) 
    yield t 
 
    t += 100
    print ('Second result is ',t) 
    yield t 
 
    t += 100
    print('Third result is ',t) 
    yield t 

x = gene()

print(type(x))


for each in x:
    pass

a = (x*x for x in range(10))

print(type(a))

b = []

for each in a:
    b.append(each)

print(b)

c = (0,)


print(type(c))

#unpacking 
latitudes = (0.34344,0.98564)
passports = [("USA","987487"),("INDIA","098736"),("CHINA","9093843")]

for country in sorted(passports):
    print(type(country))
    print("%s/%s" % country)

print(passports)
passports.sort()
print(passports)


















print("I am adding a new line at the end")























