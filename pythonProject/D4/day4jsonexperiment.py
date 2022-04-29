import json
"""
comment 
"""

shaun = {
    "address": "yobo street",
    "town": "My town",
    "postcode": "A1 2BC"
}
## triple can be used for a comment or a multiple line piece of code
s =  """
   [
        {
        "make":"Ford",
        "model":"Fiesta",
        "colour": "Black",
        "registration": "AA01 1BC"
        },
        {
        "make": "Feord",
        "model":"Feiesta",
        "colour": "Belack",
        "registration": "EA01 1BC"
        }  
    ]
"""

j = json.loads(s)
print(j)

cars = json.loads(s)
print(cars)

for car in cars:
    print(car["make"], car["model"])