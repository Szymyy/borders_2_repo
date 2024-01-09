import pygame
import button
import graphics_handler
import game

pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size
clock = pygame.time.Clock()

menu_graphics = graphics_handler.Graphics_Handler()
buttons = []

def menu():
  background = pygame.image.load("Background test.png")
  menu_events = pygame.event.get()
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  menu_graphics.render_objects()
  event_handler(menu_events, buttons)
  pygame.display.update()

current_state = menu

def state_game():
  current_state = game

game_button = button.Button((125,50), (255,255), (255,255,255), state_game, window)
buttons.append(game_button)
menu_graphics.add_object(False, game_button)

# the event handler takes all the events happening in the current game-state function and handles them appropriately, currently just checks for mouse clicks
def event_handler(events, buttons):
  for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
      for Button in buttons:
        Button.is_clicked()

running = True

while running:
  current_state()
  clock.tick(20) # limits the game to 20 fps



