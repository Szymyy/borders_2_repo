import pygame
import random

class Traveller():
  def __init__(self):
    self.firstname = ""
    self.surname = ""
    self.DOB = []
    self.face = ""
    self.documents = []

  def random_firstname(self):
    firstnames = open("names/firstnames.txt")

    names = firstnames.readlines()
    position = random.randint(1,50)
    self.firstname = names[position]

    firstnames.close()

  def random_surname(self):
    surnames = open("names/surnames.txt")

    names = surnames.readlines()
    position = random.randint(1,50)
    self.surname = names[position]

    surnames.close()

  def random_DOB(self):
    DOB = []
    Age = 0
    Year = 3000
    X = random.randint(0,140)
    Age = (1200/(X+10))+10
    Year = Year - int(Age)
    Day = random.randint(1,31)
    Month = random.randint(1,12)
    if Month == 2 and Day > 28:
      Day = 28
    elif Month % 2 != 0 and Day > 30:
      Day = 30

    DOB.append(Day)
    DOB.append(Month)
    DOB.append(Year)

    self.DOB = DOB
  
  def randomise(self):
    self.random_firstname()
    self.random_surname()
    self.random_DOB()
    
      
    