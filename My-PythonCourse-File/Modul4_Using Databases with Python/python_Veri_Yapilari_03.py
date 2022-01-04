import fibo
import sys

fibo.fib(5)
fibo.fib2(4)
print(fibo.fib2(4))

print('dosya ismi:' , sys.argv[0])
# print(fibo.fib2(int(sys.argv[1]))) # calismiyor

f= open ('bilgisayar.txt', 'w')
f.write ('Mehmet Yilmaz\nThis is a test message.\n')
f.close()
f = open('bilgisayar.txt', 'r')
print(f.read())
f.close()

f = open('bilgisayar.txt', 'r')
for line in f:
    print(line, end='')
    print('Sonraki satir:')
f.close()
 



