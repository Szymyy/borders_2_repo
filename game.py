import pygame
import button 
import graphics_handler
import events_handler

game_graphics = graphics_handler.Graphics_Handler()
game_events = events_handler.Events_Handler()
buttons = []

window = pygame.display.set_mode((500, 500))

def game():
  background = pygame.image.load("Background test.png")
  window.blit(background,(0,0))
  
  game_events.update_buttons(buttons)
  game_events.update_events(pygame.event.get())
  game_events.manage_events()

  game_graphics.render_objects()
  
  pygame.display.update()

