import pygame
pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size
clock = pygame.time.Clock()



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
    self.funtion




button_1 = button((50,50),(225,225), (255,255,255), 0)
buttons = []
buttons.append(button_1)
# initalises an itnitial button object for testing



def menu():
  menu_buttons = [button_1]
  menu_events = pygame.event.get()
  # for the time being the event handler will have to take menu_buttons as a parameter
  event_handler(menu_events, menu_buttons)
  background = pygame.image.load("Background test.png")
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  pygame.display.update()



# the event handler takes all the events happening in the current game-state function and handles them appropriately, currently just checks for mouse clikcs
def event_handler(events, menu_buttons):
  for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
      button_press_area(menu_buttons, pygame.mouse.get_pos())



# the button press area function checks if the cursor was over a button at time of pressing and returns the buttons function if so
def button_press_area(mouse):
  for button in buttons:
    if mouse[0] > button.location[0] and mouse[0] <= button.location[0] + button.size[0]:
      if mouse[1] > button.location[1] and mouse[1] <= button.location[1] + button.size[1]:
        button.clicked()



running = True
while running:
  menu()
  clock.tick(30) # limits the game to 30 fps

