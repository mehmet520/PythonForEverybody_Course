from collections import deque
print(ord('H'))
asc1=ord('e')
print(asc1)
asc2=ord('4')
print('4: ', asc2)
asc = chr(42)
print('42: ', asc)
print(chr(108)+chr(105)+chr(115)+chr(116))

asc_return= ord('\n')
print(asc_return)
print(ord('5'))

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(1024)
    if len(data) < 1: break
    mystring = data.decode('utf-8')
    print(mystring)
