# practice.py is for coding practice, challenges, etc.

# create one variable of each of the four types
boolean = True
boolean = False
string = "hello world"
integer = 8
integer = 0
integer = -5
float = 656.768
string = "summer is almost over"

def addMultiply(num1, num2, num3):
  # calculate num1 + num2 and store that into a variable called result
  result = num1 + num2
  # calculate result times num3 and store that into result
  result = result * num3
  return result

mathAnswer = addMultiply(2, 4, 6)
if mathAnswer > 10:
  print("WOW")
else:
  print("meh")


# create a function called multiplyPairs
# this function will take in four variables:
# num1, num2, num3, num4
# inside the function, calculate num1 * num2
# and then also num3 * num4
# then return the product which was greater
def multiplyPairs(num1, num2, num3, num4):
  
  if num1 * num2 > num3 * num4:
    return num1 * num2
  else:
    return num3 * num4
    




# create a function called above100
# which takes in two variables: num1 and num2
# the goal of this function will be to determine if the sum of num1 and num2
# is ABOVE 100
# if it is, return True
# otherwise, return False

def above100(num1, num2):

  if num1 + num2 > 100:
    return True 
  else:
    return False






# create a variable called points and set it equal to 100
# then create a variable called highScore and set it equal to 1000
# if points is greatre than highScore, set highScore equal to points
points = 100
highScore = 1000
if points > highScore:
  highScore = points

# create a function called increasePoints
# which takes in a variable called amount
  # and increases points by amount

def increasePoints(amount):
  points += amount



# CHANGING VARIABLES
  
# create an int variable, call it anything, give it any number
# then add 10 to it 
# then multiply it by 3
# then subtract 8 from it
# then divide it by 2
yay = 37
yay += 10
yay *= 3
yay -= 8
yay /= 2


# CHANGING VARIABLES BASED ON OTHER VARIABLES

p1points = 10
p2points = p1points + 20

p2points += 20

# DETECTING IF SOMETHING IS PRESENT OR ABSENT IN A LIST
# 
# create a function called findKoala which takes in a variable called animals
# animals will be a list of strings, i.e. ["Zebra", "Panda", "Koala"]
# this function will return True if "Koala" appears in the list at least once
# and returns False otherwise
# HINT: use a for loop!
def findKoala(animals):
  print("before loop")
  for animal in animals:
    print(animal)
    if animal == "Koala":
      return True
  print("after loop")
  return False # NOTE: this must be AFTER the loop; otherwise we will return False after finding ONE item that is not a Koala, instead of checking that ALL of them are not Koala

myAnimals = ["Dog", "Cat", "Fish"]
result = findKoala(myAnimals)
# otherAnimals = ["Bat", "Mouse", "Cow"]
# result = findKoala(otherAnimals)
print(result)