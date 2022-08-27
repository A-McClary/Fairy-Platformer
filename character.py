import pygame

# whether or not we display hitboxes
debug = True

class Character:
 # Constructor function
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
    self.speedy = 0
    self.speedx = 0
    self.consumed = False
    # update this character's hitbox
    self.hitbox = pygame.Rect(self.screenx + self.hitboxOffsetX, self.screeny + self.hitboxOffsetY, self.hitboxW, self.hitboxH)

    self.isportal = False

  def draw(self, cameraX, cameraY, screen):

    # update this character's screen coordinates
    self.screenx = self.x - cameraX
    self.screeny = self.y - cameraY

    # update this character's hitbox
    self.hitbox = pygame.Rect(self.screenx + self.hitboxOffsetX, self.screeny + self.hitboxOffsetY, self.hitboxW, self.hitboxH)

    # draw this character
    screen.blit(self.image, (self.screenx, self.screeny))

    # draw hitboxes (if debug is enabled)
    if debug == True:      
      pygame.draw.rect(screen, (255, 0, 0), self.hitbox, width=10) 
# def shoot():
  