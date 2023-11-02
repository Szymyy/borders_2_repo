import pygame
pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size

class button():
  # takes in the list of the x and y size of the button and a list of 
  # the x and y coordinates of the button
  # graphics will currently pass the RGB code for a colour of a button
  def __init__(self, size, location, graphics, function):
    self.size = size
    self.location = location
    self.graphics = graphics
    self.function = function

  def if_clicked(self):
    self.funtion

button_1 = button((50,50),(225,225), 0, 0)
buttons = []
buttons.append(button_1)
# initalises an itnitial button object for testing

def menu():
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      for button in buttons:
        
  background = pygame.image.load("Background test.png")
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  
  pygame.display.update()

running = True
while running:
  menu()


