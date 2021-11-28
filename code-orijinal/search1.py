fhand = open('mbox-short.txt')
# print (fhand)
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
