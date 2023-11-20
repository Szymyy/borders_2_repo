import pygame
import button

pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size
clock = pygame.time.Clock()

def test():
  print("I work")
button_1 = button.Button((50,50),(125,125), (255,255,255), test, window)

buttons = []
buttons.append(button_1)
# initalises an itnitial button object for testing

def menu():
  background = pygame.image.load("Background test.png")
  menu_buttons = [button_1]
  menu_events = pygame.event.get()
  event_handler(menu_events, menu_buttons)
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  for Button in menu_buttons:
    Button.draw()
  pygame.display.update()

# the event handler takes all the events happening in the current game-state function and handles them appropriately, currently just checks for mouse clikcs
def event_handler(events, buttons):
  for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
      for Button in buttons:
        Button.is_clicked()

running = True
while running:
  menu()
  clock.tick(20) # limits the game to 20 fps

