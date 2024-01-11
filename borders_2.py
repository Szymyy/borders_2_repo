import pygame
import button
import graphics_handler
import event_handler

pygame.init()
# imports the pygame library used for the project
window = pygame.display.set_mode((500, 500))
# sets the window size
clock = pygame.time.Clock()

menu_graphics = graphics_handler.Graphics_Handler()
menu_events = event_handler.Event_Handler()
buttons = []

def menu():
  background = pygame.image.load("Background test.png")
  title = pygame.image.load("Title test.png")
  window.blit(background,(0,0))
  window.blit(title,(125,50))
  
  menu_events.update_buttons(buttons)
  menu_events.update_events(pygame.event.get())
  menu_events.manage_events()
  
  menu_graphics.render_objects()
  
  pygame.display.update()

current_state = menu

def state_game():
  print("womp womp")

game_button = button.Button((125,50), (255,255), (255,255,255), state_game, window)
buttons.append(game_button)
menu_graphics.add_object(False, game_button)

running = True

while running:
  menu()
  clock.tick(30) # limits the game to 30 fps



