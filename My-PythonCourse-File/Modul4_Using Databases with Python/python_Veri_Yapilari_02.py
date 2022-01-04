l=[1,2,3]
m=[[1,3,5], [3,4,5],l]
print(m)
l[1]= 100
print (m)
k=[[[1,2,3], [2,3,4]], [[1,2,3],[1,1,1]],[[1,1]]]
print(k)
print(m)
mt= [[row[i] for row in m] for i in range(3)]
print(mt)
mt = [[row[i] for row in m] for i in range(3)]
print(mt)

del(k[1])
print(k)

l =[1,2,4]
t=(1,2,3)
print(t)
print(l)
l[2]= 10
print(l)
# t[2]=10
# print(t)
x,y,z=t
print(x)
print(y)
print(z)
z=10
t=(x,y,z) # yeni tuple olusturuldu.
print(t)
v=([1,2,3], [3,2,1])
print(v)
v[0][1]=100
print (v)
t2= 1,2,3
print(t2)

l= [1,2,3] # liste
t=(1,2,3) # kayit
k={1,2,3} # kumeler set: curly bracket curly bracket
print(l)
print(t)
print(k)

l= [1,2,3,1,2,1,3] # liste
t=(1,2,3) # kayit
k={1,2,3,1,2,1,3} # kumeler set: curly bracket curly bracket
print(l)
print(t)
print(k)

k2 = set(l)
k3= set([1,2,3,1,34,3])
print(k2)
print(k3)

k4= set('bilgisayarkavramlari')
k5 = set('Mehmetyilmaz')
print(k4)
print(k5)

print(k4|k5) # | set union , birlesim islemi
print(k4-k5) # kume farki
print(k4&k5) # kesisim
print(k4^k5) # exclusiv or ozel veya, iki yonlu kume farkinin birlesimi
# yani her iki kumede de ozel olan elemanlari aliyor; ortak olanlari atiyor
l=[1,19,3,2,1]
print(l[3])
tel = {'jack': 4098, 'sape': 4139}
print(tel['sape'])
d=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
for k,v in d.items():
    print (k,v)
for i, v in enumerate (['Wochentags:','Montag', 'Dienstag', 'Mitwoch', 'Donerstag', 'Fritag', 'Samstag', 'Sontag']):
    print(i,v)

basket=['apple', 'orange', 'apple', 'pear','orange', 'banaba']
a=set(basket) # KUME:set komutu listeyi kumeye  donusturuyor
print(a)
k=sorted(set(basket)) # LISTE: kumenin sirali olmasi gerekmedigi icin, sorted yapinca listeye donusturuluyor

print(k)
for f in sorted(set(basket)):
    print(f)
