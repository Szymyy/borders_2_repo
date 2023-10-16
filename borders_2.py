import pygame
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size

class button():
  # takes in the list of the x and y size of the button and a list of 
  # the x and y coordinates of the button
  def __init__(self, size, location):
    self.size = size
    self.location = location

button_1 = button((50,50),(225,225))
# initalises an itnitial button object for testing


def menu():
  background = pygame.image.load("Background test.png")
  title = pygame.image.load("Title test.png")
  button = pygame.image.load("Button test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  window.blit(button,button_1.location)
  pygame.display.update()

menu()

