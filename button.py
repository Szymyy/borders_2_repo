import pygame

class button():
  # takes in the list of the x and y size of the button and a list of 
  # the x and y coordinates of the button
  # graphics will currently pass the RGB code for a colour of a button
  def __init__(self, size, location, graphics, function):
    self.size = size
    self.location = location
    self.graphics = graphics
    self.function = function

  def clicked(self):
    self.function()
