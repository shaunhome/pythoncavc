import random
# Random numbers:

#n = random.randint(1, 1000)
#print(n)

#for i in range(1, 7):
 #   s = random.randint(1, 49)
  #  print(s)

# ((pick a number..
#n = random.randint(1, 100)

# loop....
#while guess !=n:

 #get input from user
#guess = input("guess a number...")

# conditional statement: wrong or right
#if guess ==n:
 #   print("You got it right")

 #))

 ## have a go

n= random.randint(1,11)

guess = 0
while guess !=n:
    s = input("Guess a number please:_____")
    print("You guessed "+ s)

    if s.isnumeric():

        guess = int(s)


        if guess == n:
            print("Congrats you guessed correctly")
        elif guess>n:
            print("Too high")
        elif guess<n:
            print("Too low")

    else:
        print("This isn't a number, please enter a numeric.")
