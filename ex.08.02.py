fname= input('Enter file name: ')
if len(fname) < 1:
    fname = "mbox-short.txt"
fh=open(fname)
count=0
#lst=list()
for line in fh:
    if line.startswith('From:'): continue
    if line.startswith('From'):
        count=count+1
        words=line.split()
    # email=words[1]
        print (words[1])
#    if email in lst:continue
#    lst.append(email)
#print (lst)
print('There were', count , 'lines in the file with From as the first word')


