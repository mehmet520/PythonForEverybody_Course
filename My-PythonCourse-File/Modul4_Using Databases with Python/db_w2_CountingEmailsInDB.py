import sqlite3

conn = sqlite3.connect('db_w2_CountingEmailsInDB.sqlite')
print('conn: ', conn)
cur = conn.cursor()
print('cur: ', cur)
cur.execute ('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
fname = 'mbox-short.txt'
fh = open (fname)
print('fh: ', fh)
for line in fh:
    # print(line)
    if not line.startswith('From: '): continue
    pieces = line.split()                       # List
    # print('\npieces: ', pieces)
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    # print('email: ', email, 'row: ', row)
    
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    # conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr_cmd = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
sqlstr = cur.execute(sqlstr_cmd)
print('\n sql_string: ', sqlstr)

print('\nsql_strring (sqlstr) (row) objekt (library): \n')
for row in sqlstr:
    print(row)
    # print(str(row[0]), row[1])

# print('\n sql_string2: ', sqlstr)
# sqlstr = cur.execute(sqlstr_cmd)

print('\nEmail Count Table:\n')
for row in sqlstr: # 2.kez çalışmıyor. sqlstr yerine 'cur.execute(sqlstr_cmd)' yazmak gerekiyor.
    # print('\nrow objekt list: \n', row)
    print(str(row[0]), row[1])

# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

cur.close()
conn.commit()

