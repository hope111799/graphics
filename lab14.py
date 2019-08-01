# -------------------------------------------------
#        Name: <VIC BROWN and LILIANA LINAN>
#    Filename: lab14.py
#        Date: <July 30, 2019>
#
# Description: < Making Graphics>
# -------------------------------------------------

from graphics import *   
###Orignal circle graphic
##def main():
##
##  win = GraphWin("My Circle", 600, 400)   #Open new graphics window #Inside parenthesis (name, width, height)
##  c = Circle(Point(50,50), 10) #Create circle object in memory and add coordinates and radius
##  c.draw(win) #Draw circle in graphics window 
##  win.getMouse()    # Pause to view result
##  win.close()    # Close window when done

def main():
  #open the graphic window.
  win = GraphWin( "Lab 7 Demo", 600, 400 )

  # create and draw a red circle
  center = Point( 100, 100 )
  circ = Circle( center, 30 )
  circ.setFill( 'red' )
  circ.draw( win )
  
  # add a label inside the circle
  label = Text( Point( 100, 100 ), "red circle" )
  label.draw( win )

  # create and draw a rectangle
  rect = Rectangle( Point( 30, 70 ), Point( 50, 200 ) )
  rect.draw( win )
  win.getMouse() # Pause to view result
  win.close() # Close window when done


main()
