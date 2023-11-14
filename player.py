from graphics import *
import time
import random

# --- classes ---

class Player:
    def __init__(self, win, position):
        self.direction = -1

        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)

        self.p1 = Point(position.getX(), position.getY())

        self.body = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None

        self.construct(position)
        self.px = position.getX()
        self.py = position.getY()

    def construct(self, position):
      avatar = Image(Point(position.getX(), position.getY()), "images/Down.png")
      self.body = avatar 
      
    def redrawleft(self, win, position):
      self.undraw() 
      avatarleft = Image(Point(position.getX(), position.getY()), "images/Left.png")
      self.body = avatarleft
      self.body.draw(win)

    def redrawright(self, win, position):
      self.undraw() 
      avatarright = Image(Point(position.getX(), position.getY()), "images/Right.png")
      self.body = avatarright
      self.body.draw(win)
      
    def redrawup(self, win, position):
      self.undraw() 
      avatarup = Image(Point(position.getX(), position.getY()), "images/Up.png")
      self.body = avatarup
      self.body.draw(win)
      
    def redrawdown(self, win, position):
      self.undraw() 
      avatardown = Image(Point(position.getX(), position.getY()), "images/Down.png")
      self.body = avatardown
      self.body.draw(win)
  
    def draw(self, win):
        self.body.draw(win)

    def undraw(self):
        self.body.undraw()

    def move(self, dx, dy):
        self.body.move(dx, dy)
        self.px = self.px + dx
        self.py = self.py + dy   
        print(self.px, self.py)


