import xml.etree.ElementTree as ET
input='''<stuff>
    <users>
        <user x='2'>
            <id> 001</id>
            <name>Mehmet</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring (input)
lst = stuff.findall ('users/user')

print('\ninput: ', input)
print('\nstuf : ', stuff)
print('\nUser count:', len(lst))
print('\nlst :', lst)
for item in lst:
    print('\nName ', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
    print()



