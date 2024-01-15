import pygame
import random

class Traveller():
  def __init__(self):
    self.firstname = ""
    self.surname = ""
    self.DOB = ""
    self.face = ""
    self.documents = []

  def randomise(self):
    firstnames = open("names/firstnames.txt")
    
    names = firstnames.readlines()
    position = random.randint(1,50)
    self.firstname = names[position]
    firstnames.close()

    surnames = open("names/surnames.txt")
    
    names = surnames.readlines()
    position = random.randint(1,50)
    self.surname = names[position]
    surnames.close()

    