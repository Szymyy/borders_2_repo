import pygame
class Button():
  # takes in the list of the x and y size of the button and a list of 
  # the x and y coordinates of the button
  # graphics will currently pass the RGB code for a colour of a button
  def __init__(self, size, location, graphics, function, surface):
    self.size = size
    self.location = location
    self.graphics = graphics
    self.function = function
    self.surface = surface

  def is_clicked(self):
    pos = pygame.mouse.get_pos()
    if pos[0] > self.location[0] and pos[0] < self.location[0] + self.size[0]:
      if pos[1] > self.location[1] and pos[1] < self.location[1] + self.size[1]:
        self.function()


  def draw(self):
    pygame.draw.rect(self.surface, self.graphics, (self.location, self.size))