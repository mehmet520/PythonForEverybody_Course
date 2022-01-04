import sqlite3
connection = sqlite3.connect('db_w2_exam2_CountingOrganisation.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute ('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('\nEnter file name: ')
if len(fname) < 1: fname = 'mbox.txt'
# fname = 'mbox-short.txt'
fhand = open (fname)
print('fhand:', fhand)
x=0
for line in fhand:
    if not line.startswith('From: '): continue
    # print('line: ', line)
    words = line.split()
    email = words[1]
    start= email.find('@')
    org = email[start+1:]
    # print('org: ', org)
    cursor.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    raw = cursor.fetchone()
    if raw is None:
        cursor.execute('''
        INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cursor.execute('''
        UPDATE  Counts SET count = count + 1 WHERE org = ?''', (org,))
    x = x + 1
    # if x > 10: connection.commit()
# cursor.execute('SELECT org, count FROM Counts ORDER BY count DESC')
sqlstr = ('SELECT org, count FROM Counts ORDER BY count DESC')
for row in cursor.execute(sqlstr):
    print ('row: ', row)
cursor.close()
connection.commit()
