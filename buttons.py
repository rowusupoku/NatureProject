from graphics import *

class Buttons: 
  def __init__ (self, win, position1, position2):
    
    self.__next= None
    self.construct(position1, position2)
    self.__win = win
  
  def construct(self, position1, position2):
    
    self.b1 = Point(position1.getX(), position1.getY())
    self.b2 = Point(position2.getX(), position2.getY())
  
    self.__next = Rectangle(self.b1, self.b2) 
    self.__next.setFill("")
    self.__next.setOutline("")

  
    
  def draw(self, win):
    
    self.__next.draw(win)
    
  def undraw(self):
    self.__next.undraw()
  
  def inside(self, win, position, rectangle):

    return self.b1.getX() <= position.getX() <= self.b2.getX() and self.b1.getY() <= position.getY() <= self.b2.getY() 
