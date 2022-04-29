from datetime import datetime

rightnow = datetime.now() #get current date and time
print(rightnow)
print(rightnow.weekday()) #gives a day of the week from 0-6

firstdate = datetime(1989, 8, 22, 15, 30, 15) #constructs a date
print(firstdate)
print(firstdate.weekday())

seconddate = datetime(1993, 12, 2) #constructs with a default time/midknight
print(seconddate)

if firstdate < seconddate: #compare two dates
    print("first date is earlier")
else:
    print("second date is earlier")

s = seconddate.strftime("%d of %B, %Y was a %A")
print(s)

if firstdate == seconddate:
    print("they're both the same")
else:
    print("they're not both the same")

dates= [(1923, 5, 7), (1956, 2, 9), (2004, 4, 19), (1978, 10, 13), (1834, 6, 19)]

for dt in dates:
    d = datetime(*dt) #* will expand the date into the full ISO 8601 format.
    print("{} : {}".format(d, d.weekday()))
    #list will print in this format; a block: another block.format with this and then this
    # carry on from 23.10

### how to prep for a coding project.
#Requirement
#- read the briefing, make sure you understand it
#- ask any questions that you might have



#Analysis
#- write out the problem in "pseudocode"
#- draw a diagram of the problem - formal modelling languages : flowcharts, UML, BPMN)



#Design
#- turn pseudocode into Python code structures
#- decide what kind of application it is (web application, mobile app, desktop app, ...)
#- decide on other tools/functions used by the program (databases, files, devices, ...)



#Code
#- write code according to the design
#- organise projects in our IDE
#- version control repository (Github, Svn, ...)



#Test
#- unit testing - testing small pieces of code as we develop them
#- testing framework - Java:JUnit, C#:NUnit, Python:Pytest



#Deploy
#- integrate our code together with other code developed by our team / third party code
#- pass it on to our customers

