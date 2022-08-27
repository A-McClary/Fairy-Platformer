from character import *
def createPortal(x, y, platformList):
  Portal = Character(x, y, 250, 250, 50, 50, 150, 150, "Assets/Items/Portal.png")
  # set the isPortal property of Portal to True
  Portal.isportal = True
  platformList.append(Portal)