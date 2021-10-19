# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count= 0
numtotal=0
for line in fh:
    line= (line.rstrip())
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    count = count +1
    #print(count)
    numstart=line.find ('0')
    #print (numstart)
    num=float(line [numstart:])
    numtotal= numtotal+num
    #print(numtotal)
print('Average spam confidence:', numtotal/count)