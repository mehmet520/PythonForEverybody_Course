import sqlite3
conn = sqlite3.connect('db.db')

c= conn.cursor()
# Create table
# c.execute(''' CREATE TABLE stocks
            # (date text, trans text, symbol text, qty real, price real)''')

# inp = input('Europa floor: ?\n')
# usf = int(inp) + 1
# print ('US floor: ', usf)
y= list()
capabilities = dir(y) # The dir() command lists capabilities
# print(capabilities) # the methods (messages) used with list object

class PartyAnimal:      # Class: A template
    x = 0               # Attribute: A variable within a class - özellik adi, boyu vb.

    def __init__(self, nam):     # Method(Message): A function within a class
        self.name = nam          # Attribute: A variable within a class - özellik adi, boyu vb.
        print(self.name, ' constructed\n')

    def party(self):        # Method(Message): A function within a class
        self.x = self.x + 1 # Attribute: A variable within a class - özellik adi, boyu vb.
        print(self.name, 'So far party count: ', self.x)

    def __del__(self):      # Method(Message): A function within a class
        print(self.name, ' destructed:  ', self.x)

class FootballFan(PartyAnimal):         # Inheritance: The ability to extend a class to make a new class.
    points = 0                  # Attribute: A variable within a class - özellik adi, boyu vb.
    def touchdown(self):        # Method(Message): A function within a class
        self.points = self.points + 7   # Attribute: A variable within a class - özellik adi, boyu vb.
        self.party()
        print(self.name, ' points ', self.points)
 
s = PartyAnimal('Sally')    # Constructer: Code that runs when an objekt is created.
# Object (Sally): A particular instance of a class
s.party() # So far 1
s.party() # So far 2
s.party() # So far 3
PartyAnimal.party(s) # So far 4

j = FootballFan('Jim')  # Constructer: Code that runs when an objekt is created.
# Object (Jim): A particular instance of a class
j.party()
j.touchdown()


print('\nType of an object:\n ', type(s))
print('\nDir (Capabilities) of an object: \n\n', dir(s))

s = 42
print('\n an contains:    ' , s)
print('\nType of an object:\n ', type(s))
print('\nDir (Capabilities) of an object: \n\n', dir(s))
print()

class SpaceAnimal():        # Class: A template
    x = 0                   # Attribute: A variable within a class - özellik adi, boyu vb.
    name = ''               # Attribute: A variable within a class - özellik adi, boyu vb.
    def __init__(self, z):  # Method(Message): A function within a class
        self.name = z       # Attribute: A variable within a class - özellik adi, boyu vb.
        print(self.name, ' constructed\n')

    def party(self):
        self.x = self.x + 1 # Attribute: A variable within a class - özellik adi, boyu vb.
        print(self.name, ' party count is: ', self.x)
     
s = SpaceAnimal('Sally') # Constructer: Code that runs when an objekt is created.
# Object (Sally): A particular instance of a class
s.party()

j= SpaceAnimal('Jim')   # Constructer: Code that runs when an objekt is created.
j.party()
s.party()

