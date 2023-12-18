import pygame
import button 
import graphics_handler

game_graphics = graphics_handler.graphics_handler()
buttons = []

def game(surf):
  background = pygame.image.load("Background test.png")
  surf.blit(background,(0,0))
  game_graphics.render_objects()
  game_events = pygame.event.get()
  event_handler(game_events, buttons)
  pygame.display.update()

def event_handler(events, buttons):
  for event in events:
    if event.type == pygame.MOUSEBUTTONDOWN:
      for Button in buttons:
        Button.is_clicked()
