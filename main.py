practiceOnly = False
if practiceOnly:  
  from practice import *
  quit()

# NOTE: whenever you change something's x and y, make sure to also update the hitbox!

# import external libraries
import pygame
import random
import time

# import internal libraries ... code that we created
from character import *
from level1 import *
from level2 import *

# where the background image is (isn't this always (0,0)?)
bgworldX = 0
bgworldY = 0

# the dimensions of the world (and also the background)
worldW = 3440
worldH = 1440

# initialize pygame
pygame.init()

# allows us to use fonts in pygame
pygame.font.init() 

# load in keyboard keys
# key status - KEYDOWN or KEYUP ... pressed or released
# key name - K_SPACE, K_A, K_H, K_UP (up arrow key)
from pygame.locals import (
  KEYUP,
  KEYDOWN,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  K_SPACE,
  QUIT,
  K_a,
  K_d,
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT
)

# dimensions of the screen
screenW = 800
screenH = 600

# load background image
backgroundImg = pygame.image.load('Assets/Backgrounds/fantasy.png')
backgroundImg = pygame.transform.scale(backgroundImg, (worldW, worldH))

# Create fairy object usig character constructor function
fairy = Character(2200, 800, 131, 212, 32, 1, 75, 200, "Assets/Characters/fairy.png")
# Create owl object
owl = Character(1000, 1000, 150, 150, 20, 1, 150, 155, "Assets/Characters/SNOWY.png")
#Create snowball object
snowball = Character(1300, 1033, 142, 100, 16, 1, 99, 100, "Assets/Items/snowball.png")
last_snowball_time = time.time()
# fairy movement speed (not current speed but maximum potential speed)
# the fairy's current speed is set to this 
# LATER: use this in key processing code to set movement speed once they start moving

fairyMaxSpeed = 25

# item
star = Character(234, 567, 200, 89, 55, 2, 110, 99, "Assets/Items/star.png")

# set up the drawing window
screen = pygame.display.set_mode([screenW, screenH])

# list of platforms
active_platforms = level1_platforms

# list of owls
active_owls = level1_owls

# list of snowballs
active_snowballs = level1_snowballs
active_snowballs.append(snowball)
# run until the user preses the game window's X button (or the repl stop button)
running = True

# checks for collision between two game objects 
# assumes obj1 and obj2 both have hitbox properties
"""
def check_collision(obj1, obj2):
  obj1.collisions[0] = obj2.hitbox.collidepoint(obj1.hitbox.topleft)
  obj1.collisions[1] = obj2.hitbox.collidepoint(obj1.hitbox.topright)
  obj1.collisions[2] = obj2.hitbox.collidepoint(obj1.hitbox.bottomleft)
  obj1.collisions[3] = obj2.hitbox.collidepoint(obj1.hitbox.bottomright)
  obj1.collisions[4] = obj2.hitbox.collidepoint(obj1.hitbox.midleft)
  obj1.collisions[5] = obj2.hitbox.collidepoint(obj1.hitbox.midright)
  obj1.collisions[6] = obj2.hitbox.collidepoint(obj1.hitbox.midtop)
  obj1.collisions[7] = obj2.hitbox.collidepoint(obj1.hitbox.midbottom)
  obj1.collisions[8] = obj2.hitbox.collidepoint(obj1.hitbox.center) 
  return True in obj1.collisions
"""

globalvariable = 1

# create a function called update_level()
def update_level():
  global level, active_platforms, backgroundImg, active_owls
  level += 1
  if level == 1:
    active_platforms = level1_platforms
    active_owls = level1_owls
    backgroundImg = pygame.image.load('Assets/Backgrounds/fantasy.png')
    backgroundImg = pygame.transform.scale(backgroundImg, (worldW, worldH))
  if level == 2:
    active_platforms = level2_platforms
    backgroundImg = pygame.image.load("Assets/Backgrounds/ocean.png")
    backgroundImg = pygame.transform.scale(backgroundImg, (worldW, worldH))

# creates a specific font that we can reuse later
font = pygame.font.SysFont('Chewy', 30)

# what level we are currently on
level = 1

# main game loop
# this is like a forever loop from Scratch!
# the main game loop mainly does three things:
# 1 - process user inputs (mouse and keyboard)
# 2 - update stuff in the game usually by moving them or handling collisions
# 3 - draw everything
while running:
  
  # make camera follow fairy
  cameraX = fairy.x - (screenW/2) + (fairy.w/2)
  cameraY = fairy.y - (screenH/2) + (fairy.h/2)  

  # update position of background image, for scrolling background
  bgscreenX = bgworldX - cameraX
  bgscreenY = bgworldY - cameraY
  
  # display background
  screen.blit(backgroundImg, (bgscreenX,bgscreenY))   

  # display fairy
  fairy.draw(cameraX, cameraY, screen)
  
  # display owl
  owl.draw(cameraX, cameraY, screen)
  
  # display snowball
  
  for snowball in active_snowballs:
    snowball.draw(cameraX, cameraY, screen)
    snowball.x += 3
    collide = fairy.hitbox.colliderect(snowball.hitbox)
    if collied:
      fairy.x = 2200
      fairy.y = 800
      snowball.kill()
  # display star and its hitbox (if not consumed)
  if star.consumed == False:
    star.draw(cameraX, cameraY, screen)
           
  # process keyboard events
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_SPACE:
        pass
      if event.key == K_a:
        pass
      if event.key == K_d:
        pass
      if event.key == K_UP:
        fairy.speedy = -fairyMaxSpeed      
      if event.key == K_DOWN:
        fairy.speedy = fairyMaxSpeed
      if event.key == K_LEFT:
        fairy.speedx = -fairyMaxSpeed      
      if event.key == K_RIGHT:
        fairy.speedx = fairyMaxSpeed
    if event.type == KEYUP:
      if event.key == K_a:
        pass
      if event.key == K_d:
        pass
      if event.key == K_UP:
        fairy.speedy = 0      
      if event.key == K_DOWN:
        fairy.speedy = 0
      if event.key == K_LEFT:
        fairy.speedx = 0      
      if event.key == K_RIGHT:
        fairy.speedx = 0    
    if event.type == pygame.QUIT:
      running = False

  # move fairy based on her speed
  fairy.x = fairy.x + fairy.speedx
  fairy.hitbox.x = fairy.hitbox.x + fairy.speedx
  fairy.y = fairy.y + fairy.speedy  
  fairy.hitbox.y = fairy.hitbox.y + fairy.speedy

  # check if fairy is colliding with any platforms
  # also draw the platforms
  physically_colliding = False
  for platform in active_platforms:    
    collide = fairy.hitbox.colliderect(platform.hitbox)
    if collide:
      if platform.isportal:
        update_level()
        break
      else:        
        physically_colliding = True    
    platform.draw(cameraX, cameraY, screen)

  for owl in active_owls:      
    owl.draw(cameraX, cameraY, screen)
  # if fairy is colliding with any platforms, scoot fairy back
  # to prevent the fairy from going inside the platform
  if physically_colliding:
    fairy.x = fairy.x - fairy.speedx
    fairy.hitbox.x = fairy.hitbox.x - fairy.speedx
    fairy.y = fairy.y - fairy.speedy
    fairy.hitbox.y = fairy.hitbox.y - fairy.speedy

  # get the center coordinates of the fairy
  centerx = fairy.x + fairy.w/2
  centery = fairy.y + fairy.h/2

  # check if fairy has reached edge of screen
  if centerx < screenW/2:
    fairy.speedx = 0
    centerx = screenW/2 + 1
    fairy.x = centerx - fairy.w/2
  if centery < screenH/2:
    fairy.speedy = 0    
    centery = screenH/2 + 1
    fairy.y = centery - fairy.h/2
  if centery > worldH-screenH/2:
    fairy.speedy = 0    
    centery = worldH-screenH/2 - 1
    fairy.y = centery - fairy.h/2
  if centerx > worldW-screenW/2:
    fairy.speedx = 0    
    centerx = worldW-screenW/2 - 1
    fairy.x = centerx - fairy.w/2  

  # setup debugging text
  fairy_x_text = font.render(str(fairy.x), False, (0, 0, 255))
  fairy_y_text = font.render(str(fairy.y), False, (0, 0, 255))

  # draws debugging text
  screen.blit(fairy_x_text, (50,50))
  screen.blit(fairy_y_text, (50,100))

  # update screen
  pygame.display.flip()

  # snowballs
 
  current_time = time.time()
  if current_time - last_snowball_time >= 3:
    print("snowball")
    snowball = Character(1300, 1033, 142, 100, 16, 1, 99, 100, "Assets/Items/snowball.png")
    last_snowball_time = time.time()
    active_snowballs.append(snowball)
# if this line of code is reached, game is not running, so quit
pygame.quit()

# hehehe now there is a comment(Casper the ghost did it)