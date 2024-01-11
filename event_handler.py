import pygame

class Event_Handler():
  def __init__(self):
    self.events = []
    self.buttons = []

  def update_buttons(self, buttons):
    self.buttons = buttons

  def update_events(self, events):
    self.events = events

  def manage_events(self):
    for event in self.events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        for button in self.buttons:
          button.is_clicked()

