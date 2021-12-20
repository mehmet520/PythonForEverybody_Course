# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
import re

# file_name= int (input ('Enter 1 for regex_sum_42.txt;/n 2 for regex_sum_1258375txt :\n'))
# if file_name==1: fhand= 'regex_sum_42.txt'
# elif file_name == 2: fhand= 'regex_sum_1258375.txt'
fhand= 'regex_sum_1258375.txt'
handle= open(fhand)


# handle= "Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity.  You can write programs for many reasons, ranging from making your living to solving8837 a difficult data analysis problem to having fun to helping 128someone else solve a problem.  This book assumes that everyone needs to know how to program ..."
num_list= list()
for line in handle:
    num_line_list= re.findall ('[0-9]+', line)
    num_list=num_list + num_line_list
inum= list()
isum=0
for i in num_list:
    inum.append(int(i))
    isum=isum+int(i)

print (isum)
