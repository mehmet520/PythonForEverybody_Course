import json

# data is dictionary
data = '''{
    "name" : "Mehmet",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads (data)
print('Type of info: \n', type(info))
print ('\ninfo: \n', info)
print ( "\nName: ", info ["name"])
print ('\nphone:\n', info['phone'])
print ("\nHide: ", info ["email"] ["hide"] )

#  data2 ist eine liste
data2 = '''        
[
    {"id" : "001",
    "x": "2",
    "name" : "Mehmet"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Mehmet"
    }
] '''

print ('\n\nDie andere Beispiel mit Listen:\n')
info2= json.loads (data2)
print('\nUser Count:  ', len(info2))
print('\nType of info: \n', type(info2))
print ('\ninfo2: \n', info2)            # ergibt list

for item in info2:
    print('\nId     :   ', item ['id'])
    print('Name   :   ', item ['name'])
    print('Atribute:  ', item ['x'])

print ('\nid: ', info2[0]['id'])        # info2 is a list(); info2 [0] is a dictionary
dictionary= info2[0]                             # d is a dictionary
print ('Erste Element der Liste = Dictionary:   ',  dictionary)
print('\nName: ', dictionary['name'])