# How functions work.


def hello(sName):
    print(f"hello world I am {sName}")

hello("gr")
hello("BBB")
hello("gre")


def square(nInput):
    res = nInput * nInput
    return res


def multi(nFirst, nSecond):
    if type(nFirst) == int and type(nSecond) == int: ## makes sure both values entered are integers
        res = nFirst * nSecond
        return res
    else:
        return "Invalid inputs"


n = multi(1, 6)
print(n)

## SECTION 21 FOR HOMEWORK

#s = "t"
#s2 = sorted(s.lower()) # sorts all letter in str in alphabetical order
#print(s2)

#s3 = "tk"
#s4 = sorted(s3.lower())


def checkAna(s1, s2):

    # take spaces out of words

    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    # sort and lowercase

    sorted_s1 = sorted(s1.lower())
    sorted_s2 = sorted(s2.lower())
    print(sorted_s1)
    print(sorted_s2)

    # compare both

    if sorted_s1 == sorted_s2:
        return True
    else:
        return False
    # or return sorted_s1 == sorted_s2, this will result in True/False

# user input

s1 = input("Enter the first word")
s2 = input("Enter the second word")

# call function
bRes = checkAna(s1, s2)
if bRes == True:
    print("Yes, anagram")
else:
    print("NO, NOT anagram")