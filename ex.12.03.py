#  Using Python to Access Web Data- Woche 4 - 
# Chapter 12.3 - Unicode Characters and Strings

# ord () function shows ASCII codes of the characters.
print(ord('H'))
print(ord('e'))
print(ord('l'))
print(ord('o'))
print(ord('\n'))
# 72
# 101
# 108
# 111
# 10

# In Python 3, all strings internally are UNICODE
# Working with string variables in Python programs and reading data from files usually "just works" 
# When we talk to a network resource using sockets or talk to a database 
# we have to encode and decode data (usually to UTF-8)

# UNICODE Python\'da regular yani normal STRING olarak kabul edilir. b-BYTE string ise farklidir.
#type of BYTE-b string:  <class 'bytes'>
x= b'asd'
print('\ntype of bite-b string: ', type (x))

# Regular type of string:  <class 'str'>
y= 'sdf'
print('\nRegular type of string: ', type(y))

# UNIFORM type string:  <class 'str'>
z= u'dfg'
print ('\nUNIFORM type string: ', type(z))

print('UNIFORM Python\'da regular yani normal STRING olarak kabul edilir. b-byte string ise farklidir.\n')

# An HHTP Request in Python
import socket
mysock= socket.socket (socket.AF_INET, socket.SOCK_STREAM)
print ('1. mysock: ', mysock)
# 1. mysock:  <socket.socket fd=324, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

mysock.connect (('data.pr4e.org', 80))
print ('\n2. mysock: ', mysock)
# 2. mysock:  <socket.socket fd=324, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, 
# laddr=('192.168.178.41', 56195), raddr=('192.241.136.170', 80)>

# ==> encode (UTF-8): Tirnak icindeki Python'un 'UNICODE' kabul ettigi STRING'i, 
#UTF-8'e yani b-BYTE'a donusturup, sonra 'cmd' degiskenine atiyor.
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 

print('\ncmd: ', cmd)
# cmd:  b'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'

mysock.send(cmd)    # ==> mysock degiskeninin degeri degismedi, onceki ile ayni
print ('\n3. mysock: ', mysock)
# 3. mysock:  <socket.socket fd=324, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, 
# laddr=('192.168.178.41', 56195), raddr=('192.241.136.170', 80)>
print('\n\n')
x=1
data= mysock.recv(250) # ==> currency of 'data'  is BYTE
print('_________________________________________')
print ('\n', x, '. data= birimi BYTE: ', data)
x=x+1
devam= input(' \nDevam mi? ')
if len(data) < 1:
    print('bitti')
mystring= data.decode() # ==> currency of'mystring' is UNICODE ; yani decode(' UTF-8 veya ASCII' default degerini alir.) fonksiyonu BYTE'i UNICODE'a ceviriyor.
print (mystring)
devam= input(' \nDevam mi? ')
# Python Strings to Bytes
# When we talk to an external resource like a network socket 
# we sends bytes, 
# so we need to encode Python 3 strings into a given character encoding
# When we read data from an external resource, 
# we must decode it based on the character set 
# so it is properly represented in Python 3 as a string
x=1
while True: # 'BYTE'i 'UNICODE'a ceviriyor.
    data= mysock.recv(512) # ==> currency of 'data'  is BYTE
    print('_________________________________________')
    print ('\n', x, '. data= birimi BYTE: ', data)
    x=x+1
    devam= input(' \nDevam mi? ')
    if len(data) < 1:
        break
    mystring= data.decode() # ==> currency of'mystring' is UNICODE ; yani decode(' UTF-8 veya ASCII' default degerini alir.) fonksiyonu BYTE'i UNICODE'a ceviriyor.
    print (mystring)
