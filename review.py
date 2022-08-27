# review.py is for notes over Python (not coding challenges)

# what is a variable?
# store data in it

# what are the four types of variables?
# 1 - integer - any number (negatives, positives) ... just no decimal
# 2 - float - any numbers with decimal
# 3 - boolean - True or False 
# 4 - string - symbols, letters, numbers ... text

# myNumber = "578237983428977894332423402380943"
# myNumber = myNumber + 1

# what do if/else statements do?
# if-then statements ... 
# example:
# if adrianna == "cool":
#   print("sparkles")
# else:
#   print("chocolate")

# if statements check if a condition is True or False
# in other words, they evaluate whether a statement is True or False
# if the condition is True, run the code inside the if block
# if the condition is False, run the code inside the else block (if there is any)

# create one variable of each of the four types

# My variables :) WOOOOOOOOOOOOO
myFloat = 89743.32
myInt = 84784347
myInt = 0
myBoolean = True
myBoolean = False
myString = 'MerryChristmas!'


# what is a function?
# what an object does

hero.moveXY(500, 200)
hero.moveRight(2)
hero.say("Hello")
hero.attack("Shrek")
hero.cleave()



def fall():
  print("Please punch the computer now.")

def addNumbers(num1, num2, num3):
  return num1+num2+num3

addNumbers(600,5,-8)




# create a function called getSign
# make this function take in a variable called num
# the goal of this function will be to report the mathematical sign
# of the number
# "+" if its positive
# 0 if its 0
# "-" if its negative
def getSign(num):
  if num > 0:
    print("+")
  if num < 0:
    print ("-")
  if num == 0:
    print ("0")

myScore = int(input("Please enter a number: "))
getSign(myScore)

# REARRANGE EQUATION MATH NOTES
"""
y = x + 5
y - 5 = x + 5 - 5
y - 5 = x
x = y - 5
"""


import time

# in Python, time is reported in "timestamps"
# a timestamp is a VERY large number representing the number of seconds since
# Jan 1, 1970
# kinda silly but that's it works
# they don't report it in a date/time format like "Saturday August 13th 11:51 AM"
# its more like 175957849485

# to get a timestamp in python, do this:
print(time.time())

# normally, we don't care about the number inside of a timestamp
# we are more concerned with the DIFFERENCE between two timestamps
# which we can use to figure out how much time has passed between two moments

print("sup")
last_print_time = time.time()
while True:
  current_time = time.time()
  if current_time - last_print_time >= 1:
    print("sup")    
    last_print_time = time.time()


quit()







# what is a class?
# classes contain objects
# a class is a category objects
# classes categorize objects

# what is an object?
# a thing ... that is true but let's be more specific!
# an object is a/an example of a class/category

# every object of the same class has the same set of variables and functions

# examples
# every human has a name
# every school has a principal
# every country has a capital
# every city has a name
# every video game has a title


sharks = ["baby", "daddy", "mommy", "grandpa", "grandma", "cousin", "uncle", "aunt"]

# please write a for loop that prints each shark in this list
for shark in sharks:
  print(shark)



# create a function called sumNumbers
# which takes in a list variable called numbers as input
# the goal of this function will be to calculate the sum of all numbers in the list
# the function should return the sum once it's done
# some numbers
def sumNumbers(numbers):
  ssf = 0
  for num in numbers:
    ssf += num
  return ssf

myNumbers = [7, 5, 12, 8, 2]
result = sumNumbers(myNumbers)
print(result)
result = sum(myNumbers)
print(result)