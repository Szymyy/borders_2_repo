import pygame
import button 
import graphics_handler

game_graphics = graphics_handler.Graphics_Handler()
buttons = []

window = pygame.display.set_mode((500, 500))

def game():
  background = pygame.image.load("Background test.png")
  window.blit(background,(0,0))
  game_graphics.render_objects()
  game_events = pygame.event.get()
  event_handler(game_events, buttons)
  pygame.display.update()

def event_handler(events, buttons):
  for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
      for Button in buttons:
        Button.is_clicked()
