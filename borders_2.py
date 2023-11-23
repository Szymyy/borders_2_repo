import pygame
import button
import graphics_handler


pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size
clock = pygame.time.Clock()
def test():
  menu_graphics.remove_object(False, button_1)
  buttons.remove(button_1)

menu_graphics = graphics_handler.graphics_handler()
button_1 = button.Button((50,50),(125,125), (255,255,255), test, window)
buttons = []

menu_graphics.add_object(False, button_1)
buttons.append(button_1)

def menu():
  background = pygame.image.load("Background test.png")
  menu_events = pygame.event.get()
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  menu_graphics.render_objects()
  event_handler(menu_events, buttons)
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

