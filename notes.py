# notes.py is for notes about this project

# --- NOTES ABOUT INVISIBLE WALL ---

# create an invisible wall that prevents the player from going outside the world
# (see notes.py for more information)
# AKA "entering the void"
# the wall actually restricts the CAMERA's movement
# the wall has top-left corner @ (0,0)
# and has width worldW - screenW (so that the camera can't go beyond that boundary)
# and has height worldH - screenH
# however, we need to apply camera controls to the invisible wall when debugging
# since the wall starts @ (0,0), those are its world coordinates
# so to calculate screen coordinates, it is
# screenX = worldX - cameraX
# screenY = worldY - cameraY
# in this case, since worldX and worldY for the wall are both 0
# it turns screenX = -cameraX, screenY = -cameraY
# invisible_wall = pygame.Rect(-cameraX, -cameraY, worldW - screenW, worldH - # screenH)
# pygame.draw.rect(screen, (255, 0, 0), invisible_wall, width=10) 