from character import *
from portal import *
level1_platforms = []
level1_owls = []
level1_snowballs = []

# create a platform at a given world location
def createPurplePlatform(x, y):
  platform = Character(x, y, 275, 170, 46, 70, 195, 34, "Assets/Platforms/purpleline.png")
  level1_platforms.append(platform)

# create the platforms
createPurplePlatform(150,554)
createPurplePlatform(2345,845)
createPurplePlatform(2451,634)
createPurplePlatform(2543,999)
createPurplePlatform(1234,890)
createPurplePlatform(3546,657)
createPurplePlatform(2135, 433)
createPurplePlatform(2060, 983)
createPurplePlatform(1660, 833)

# create a platform at a given world location
def createStoney(x, y):
  platform = Character(x, y, 145, 108, 10, 15, 135, 68, "Assets/Platforms/Stone.png")
  level1_platforms.append(platform)

# create the Stoneys
createStoney(75,2345)
createStoney(80,1200)
createStoney(3200,1400)
createStoney(3000,20)
createStoney(765,56)
createStoney(2013,764)

# create portals for level 1
createPortal(3000, 1000, level1_platforms)





# create a owl at a given world location
def createOwl(x, y):
  owl = Character(x, y, 150, 150, 20, 1, 150, 155, "Assets/Characters/SNOWY.png")
  level1_owls.append(owl)

createOwl(1000, 1000)