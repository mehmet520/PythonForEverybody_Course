#  Using Python to Access Web Data- Woche 4 - 
# Chapter 12-03 Using urllib in Python
# Chapter 12-04 Reading Web Pages

# Using urllib in Python
# Since HTTP is so common, we have a library that does all the socket work for us 
# and makes web pages look like a file
import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen ('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print (line.decode().strip())

# Like a File
counts= dict()  # counts= {}
fhand= urllib.request.urlopen ('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words= line.decode().split()
    for word in words:
        counts [word]= counts.get (word, 0) +1
print ('counts Bibliothek: ', counts)

# Reading Web Pages
print('\nReading Web Pages : ')
import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen( 'http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print (line.decode().strip())
