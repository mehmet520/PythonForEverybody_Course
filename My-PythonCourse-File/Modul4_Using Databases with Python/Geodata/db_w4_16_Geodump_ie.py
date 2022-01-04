import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open ('where.js', 'w', 'utf-8')
fhand.write('myData = [\n')
print('\nfhand: ', fhand)
count = 0
print (type(cur))
for row in cur :
    data = str(row[1].decode())
    # print ('data: ', data)
    
    # Controling if data is available
    try:
        js = json.loads(str(data))
        # print ('\njs: ', js)
    except: continue
    # Controling if data is available
    if not ('status' in js and js['status'] == 'OK'): continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    # print('\nlatlong: ', lat, lng)
    # Controling if latitude and longitude is corect
    if lat==0 or lng ==0: continue
    # Adreess
    where = js['results'][0]['formatted_address']
    where = where.replace(" ' ", " ")
    try:
        print('\n', where, lat, lng)
        count = count + 1
        if count > 1: fhand.write(',\n')
        output = "["+ str(lat) + "," + str(lng) + " , ' " + where + " '] "
        fhand.write(output)
    except: continue

fhand.write('\n];\n')   # ; ?
cur.close()
fhand.close()
print (count, 'records written to where.js')
print ('\nOpen where.html to view the data in a browser\n')



