from graphics import *
import time
import random

class Enemy:
  def __init__(self, win, rect, color):
    self.rect = rect
    self.color = color
    
    self.rect.setFill(self.color)
    self.rect.draw(self.win)

  def move(self):
    dx = random.randint(-30, 30)
    dy = random.randint(-30, 30)
    self.rect.move(dx, dy)