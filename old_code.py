# platform.hitbox = pygame.Rect(platform.x + 97, platform.y + 60, 455, 45)
# fairy.hitbox = pygame.Rect(fairy.x + 32, fairy.y + 1, 55, 200)
# pygame.draw.rect(screen, (255, 0, 0), platform.hitbox, width=10) 
# pygame.draw.rect(screen, (255, 0, 0), fairy.hitbox, width=10)

# not in class block
# y = 10

# calling the constructor function to create a Character object
# fairy = Character(50, 100, 20, 40, "Assets/fairy.jpg")

# OLD INVISIBLE WALL CODE
"""
if cameraX < 0:
  print(cameraX)
  cameraX = 1
  fairy.speedx = 0
if cameraY < 0:
  cameraY = 1
  fairy.speedx = 0
if cameraX > worldW - screenW:
  print("right wall")
  cameraX = worldW - screenW - 1
  fairy.speedx = 0
if cameraY > worldH - screenH:
  cameraY = worldH - screenH - 1
  fairy.speedy = 0
"""

# THIS IS NOT USED ANYMORE - use Character class! :) 

"""
import pygame
class Item:
  
  def __init__(self, x, y, w, h, hitboxOffsetX, hitboxOffsetY, hitboxW, hitboxH, imageName):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.imageName = imageName
    self.hitboxOffsetX = hitboxOffsetX
    self.hitboxOffsetY = hitboxOffsetY
    self.hitboxW = hitboxW
    self.hitboxH = hitboxH 
    self.image = pygame.image.load(self.imageName)
    self.image = pygame.transform.scale(self.image, (self.w, self.h))
    self.collisions = [False, False, False, False, False, False, False, False, False]
    self.screenx = 0
    self.screeny = 0
    self.consumed = False

  def draw(self, cameraX, cameraY, screen):
    self.screenx = self.x - cameraX
    self.screeny = self.y - cameraY
    self.hitbox = pygame.Rect(self.screenx + self.hitboxOffsetX, -1 * (self.screeny + self.hitboxOffsetY), self.hitboxW, self.hitboxH)
    screen.blit(self.image, (self.screenx, -1*self.screeny))
    pygame.draw.rect(screen, (255, 0, 0), self.hitbox, width=10) 
"""


# print(check_collision(fairy,platform))
  #if fairy.collisions[4] or fairy.collisions[5]: # 4 or 5 (left/right)
   # fairy.speedx = 0
  """
  if fairy.collisions[6] or fairy.collisions[7]: # 6 or 7 (up/down)
    fairy.speedy = 0
  if fairy.collisions[0] or fairy.collisions[1] or fairy.collisions[2] or fairy.collisions[3] or fairy.collisions[4] or fairy.collisions[5] or fairy.collisions[6]:
    fairy.speedx = 0
  if fairy.collisions[0] or fairy.collisions[1] or fairy.collisions[2] or fairy.collisions[3]:
    fairy.speedx = 0
    fairy.speedy = 0
  """
  # check if fairy picked up star
  # check_collision(fairy,star)
  # if True in fairy.collisions: # if fairy picked up item
    # star.consumed = True


# create an invisible wall that prevents the player from going outside the world
# (see notes.py for more information)
# FOR NOW - we are ignoring invisible wall
# invisible_wall = pygame.Rect(-cameraX, -cameraY, worldW - screenW, worldH - screenH)
# pygame.draw.rect(screen, (255, 0, 0), invisible_wall, width=10)   
