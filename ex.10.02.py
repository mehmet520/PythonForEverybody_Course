# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.

file_name= input ('Enter file name:\n')
if len (file_name) < 1: file_name = 'mbox-short.txt'
handle = open(file_name)    # Python liest die Datei.

hour_dic= dict ()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if len (words) < 6 or words[0] != 'From' : continue
    time= words [5]
    hour= time[0:2]
    hour_dic [hour]=hour_dic.get (hour, 0) +1 # Worterbuch wird produziert.
# print(hour_dic)

hour_list= hour_dic.items ()
shour_list= sorted (hour_list)
for k, v in shour_list:
    print (k, v)
# print ( sorted ( [ (k,v) for k, v in hour_dic.items() ] ))

# print(hour_list)
# print (shour_list)