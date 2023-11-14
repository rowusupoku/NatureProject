from graphics import *
from player import *
from buttons import *
import random

WIDTH = 450
HEIGHT = 300

def main():
  
  win = GraphWin("mini graphic game", WIDTH, HEIGHT)
  background = Image(Point(225, 150), "images/Background.png")
  background.draw(win)
  
  garlicb = Buttons(win, Point(140, 140), Point(160, 160))
  garlicb.draw(win)
  rock = Image(Point(140, 150), "images/rock.png")
  rock.draw(win)

  mossb = Buttons(win, Point(360, 50), Point(380, 70))
  mossb.draw(win)
  rock = Image(Point(360, 37), "images/rock.png")
  rock.draw(win)
  
  cherryb = Buttons(win, Point(20, 160), Point(40, 180))
  cherryb.draw(win)
  cherry = Image(Point(17, 160), "images/tree.png")
  cherry.draw(win)
  
  stoneflyb = Buttons(win, Point(400, 10 ), Point(420, 30))
  stoneflyb.draw(win)
  lily = Image(Point(402, -2), "images/lily.png")
  lily.draw(win)
  
  lily2 = Image(Point(430, 80), "images/lily.png")
  lily2.draw(win)
  
  wormb = Buttons(win, Point(180, 70), Point(200, 90))
  wormb.draw(win)
  log2 = Image(Point(180, 60), "images/log.png")
  log2.draw(win)
  
  p1 = Player(win, Point(370, 218))
  p1.draw(win)

  update(15)   

  prompt = Text(Point(225, 120),"Let's go interact with nature!\n There are five hidden organisms... \n Click to begin!")
  prompt.draw(win) 
  win.getMouse()
  prompt.undraw() 


  while (win.checkMouse() == None):
    
    while True:
      clickPoint = win.checkMouse()
      keyPressed = win.getKey()
      if keyPressed == "Left":
          p1.move(-20, 0)
          p1.redrawleft(win, Point(p1.px, p1.py))
      elif keyPressed == "Right":
          p1.move(20, 0)
          p1.redrawright(win, Point(p1.px, p1.py))     
      elif keyPressed == "Up":
          p1.move(0, -20)
          p1.redrawup(win, Point(p1.px, p1.py))
      elif keyPressed == "Down":
          p1.move(0, 20)
          p1.redrawdown(win, Point(p1.px, p1.py))

      
      if garlicb.inside(win, Point(p1.px, p1.py), next):
        garlic = Image(Point(225, 150), "images/Garlic.png")
        garlic.draw(win)
        win.getMouse()
        garlic.undraw()
      elif mossb.inside(win, Point(p1.px, p1.py), next):
        moss = Image(Point(225, 150), "images/Moss.png")
        moss.draw(win)
        win.getMouse()
        moss.undraw()
      elif cherryb.inside(win, Point(p1.px, p1.py), next):
        cherry = Image(Point(225, 150), "images/Cherry.png")
        cherry.draw(win)
        win.getMouse()
        cherry.undraw()
      elif stoneflyb.inside(win, Point(p1.px, p1.py), next):
        stonefly= Image(Point(225, 150), "images/Stonefly.png")
        stonefly.draw(win)
        win.getMouse()
        stonefly.undraw()
      elif wormb.inside(win, Point(p1.px, p1.py), next):
        worm = Image(Point(225, 150), "images/Worm.png")
        worm.draw(win)
        win.getMouse()
        worm.undraw()



if __name__ == "__main__":
    main()
