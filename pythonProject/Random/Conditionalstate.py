from turtle import *
# import turtle

# if
x=10
y=11
z=60
if x>y:
    print('condition 1')
elif x>z:
    print('elseif')
else:
    print('alarm')

## else if allows to add in a condition to and else statement


#loop
#n = range(1,10)
#for i in n:
    #print(i)

#i = 1
#while i==1:
   # s=input('say 2')
   # i = int(s)

#x = 10

#if x==10:
    #for i in range(5):
       # print(x,i)
#else:
   # for i in range(10, 20):
      #  print(x, i)

for i in range(1, 13): #automatically increments i by one value
    print('________________________')
    print(f"{i} times table")
    print('________________________')
    for j in range(1, 13):
        print(f"{i} x {j} = {i*j}")
