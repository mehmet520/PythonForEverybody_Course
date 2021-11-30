import xml.etree.ElementTree as ET
data = '''<person>
    <name>Mehmet</name>
    <phone type="intl">+1 345 543 5679</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring (data)

print('\ndata: ', data)
print('\ntree: ', tree)
print('\nName: ', tree.find('name'))
print('\nName: ', tree.find('name').text)
print('\nAttribute: ', tree.find('email').get('hide', '\n'))
print()
