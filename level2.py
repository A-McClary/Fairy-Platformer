from character import *
from portal import *
level2_platforms = []


def createSeashell(x, y):
  platform = Character(x, y, 275, 170, 46, 70, 195, 34, "Assets/Platforms/seashell.png")
  level2_platforms.append(platform)

# Creating Platforms
createSeashell(335, 1033)
createSeashell(2560, 508)
createSeashell(1275, 768)
createSeashell(2073, 1033)
createSeashell(2390, 733)
createSeashell(2898, 508)
createSeashell(798, 920)
createSeashell(1698, 958)
# Creates the portal
createPortal(2973, 758, level2_platforms)