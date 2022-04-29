names = ["Shaun", "Jimmy", "Davies", "Chloe"] #list of names
colours = ("red","green", "blue") #tuple (), immutable
#for i in range(0, 4):
 #   print(names[i])

names.append("Joe") #.append means add on end of list
for name in names:
    print(name)

for i in range(a, b):
    print(i)

# dictionary {}

               #key   :    value
vegetables = {"carrot": "orange veg",
              "radish": "iunno",
              "uo":"ew"}
print(vegetables["radish"])
#"iunno"

# list of dictiontionaries

food = [vegetables]

# setting up and recalling dictionarys

julie = {"last name":"Sanders",
         "likes":"crabs",
         "hates": "un-crab-like things"}

alice = {"last name":"wonderwall",
         "likes":"yo",
         "hates": "things"}

bob = {"last name":"Quilder",
         "likes":"babs",
         "hates": "crab-like things",
       "DOB": (1990, 3, 3)}

Shaun = {"first name":"Shaun",
         "likes": "gf",
         "hates": "girlfriend's mum",
         "DOB": (2000, 7, 7)}

people = [julie, alice, bob, Shaun]

name = input("Enter a name: ")
for person in people:
    if person["first name"] == name:
        print(person)
        birthday = datetime(*person["DOB"])
        s = birthday.strftime("this person was born on %d, %B, %Y which was a %A")
        print(s)
# wrong