l=[1,2,3]
l.append(55)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
l.pop()
print(l)
l.append(2)
print(l)
l2=[44,55,66]
print(l2)
l2.append(77)
print(l2)
print(l2.pop(0))
del l2[0]
print(l2)
l2.insert(0,55)
print(l2)
l.insert(1,111)
l.append(111)
print(l)
l.remove(111)
print(l)
l.append(22)
l.append(111)
l.pop()
print(l)
print(l.index(22))
print(l.index(2))
l.append(111)
print(l.count(111))
print(l)
l.sort()
print(l)
l3=[8,9,10]
l.extend(l3)
print(l)
l.append(l3)
print(l)
l.append(98)
l1=l
print(l1)
l1.append(600)
print(l)
l4=l.copy()
l4.append(700)
print(l)
print(l4)
l5= deque([11,23,45])
print(l5)
l5.append(67)
print(l5.popleft())
print(l5)
l6=[]
for x in range(1,11):
    l6.append(x**2)
print(l6)
print(x)
squares = list(map(lambda x: x**2, range(10)))
print(squares)
y = list(map(lambda t:t**2, range(15)))
print(y)
h=list(map(lambda t:t*5, range(11)))
print(h)

def f(x):
    return x*5
l7=[4,6,7]
print(list(map(f,l7)))
print(list(map(lambda x:x*5, l7)))
l8= [x**3 for x in range(11)]
print(l8)
l8= [x**2 for x in range(1,9)]
print(l8)
l8=[x*4-6 for x in range(12)]
print(l8)
print(x)
l9=[(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print(l9)
l9= [(x,y) for x in [1,2,3] for y,z in [(1,2), (2,3), (3,4)] if x !=y]
print(l9)
l=[2,3,4,5]
print(list(map(lambda x:x+4, l)))
l2=[x**2-2 for x in l]
print(l2)
print(list(map(lambda x:x*4+5, l2)))
print(list(map(lambda d:d**2-5, l)))
for x in range(1,9):
    l.append(x)
print(l)