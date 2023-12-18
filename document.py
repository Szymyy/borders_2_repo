import random
import pygame

class Document():
  def __init__(self, size, location, graphics, surface):
    self.size = size
    self.location = location
    self.graphics = graphics
    self.surface = surface
    self.valid = True

  def draw(self):
    pygame.draw.rect(self.surface, self.graphics, (self.location, self.size))

  def randomise(self):
    a = random.randint(0,10)
    if a < 7:
      self.valid = True
      self.graphics = (0,255,0)

    else:
      self.valid = False
      self.graphics = (255,0,0)

  def accept(self):
    if self.valid:
      return True
    else:
      return False

  def deny(self):
    if self.valid:
      return False
    else:
      return True
  