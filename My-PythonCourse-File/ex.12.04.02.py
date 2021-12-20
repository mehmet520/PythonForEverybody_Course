# Using Python to Access Web Data
# Woche 4
# Worked Example: Using Urllib (Chapter 12)
import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print('\n')
counts = dict ()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts [word]= counts.get('word', 0) +1
print ('\nromeo.txt icindeki kelimeler ve kac tane oldugu counts kutuphanesi icinde gosteriliyor.\n', counts, '\n')