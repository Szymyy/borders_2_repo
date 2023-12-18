import pygame
import button
import graphics_handler
import document

pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size
clock = pygame.time.Clock()

menu_graphics = graphics_handler.graphics_handler()
buttons = []

pass_1 = document.document((50,50), (100,100), (0,255,0),window)
menu_graphics.add_object(False, pass_1)

def testing_pass():
  if pass_1.accept():
    print("True")
  else:
    print("False")

  if pass_1.deny():
    print("True")
  else:
    print("False")

def menu():
  background = pygame.image.load("Background test.png")
  menu_events = pygame.event.get()
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  menu_graphics.render_objects()
  event_handler(menu_events, buttons)
  pygame.display.update()

# the event handler takes all the events happening in the current game-state function and handles them appropriately, currently just checks for mouse clicks
def event_handler(events, buttons):
  for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
      for Button in buttons:
        Button.is_clicked()

running = True
testing_pass()

while running:
  menu()
  clock.tick(20) # limits the game to 20 fps



