# -------------------------------------------------
#        Name: <VIC BROWN and LILIANA LINAN>
#    Filename: lab14.py
#        Date: <July 30, 2019>
#
# Description: < Making Graphics>
# -------------------------------------------------
from graphics import *

def main():
     win = GraphWin("Taxi!", 600, 400) #Open window

     topRect = Rectangle(Point(200, 50), Point(400, 150))
     topRect.draw(win)
     topRect.setFill("yellow")

     bodyRect = Rectangle(Point(150, 150), Point(450, 250))
     bodyRect.draw(win)
     label = Text(Point(300,200), "TAXI")
     label.draw(win)
     bodyRect.setFill("yellow")

     windowL = Rectangle(Point (210,60), Point(290, 140))
     windowL.draw(win)
     windowL.setFill("white")

     windowR = Rectangle(Point( 310, 60), Point(390, 140))
     windowR.draw(win)
     windowR.setFill("white")


     centerL = Point(225,250)
     circ = Circle(centerL, 45)
     circ.draw(win)
     circ.setFill("black")

     
     centerR = Point(375, 250)
     circ2 = Circle(centerR, 45)
     circ2.draw(win)
     circ2.setFill("black")

     

     win.getMouse()
     win.close()


main()
