"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Geoffrey Cohen.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.delay(20)

geoff = rg.SimpleTurtle('turtle')
geoff.pen = rg.Pen('red', 30)
geoff.speed = 10

geoff.forward(200)
geoff.right(90)
geoff.forward(200)
geoff.right(90)
geoff.forward(400)
geoff.right(90)
geoff.forward(400)
geoff.right(90)
geoff.forward(400)
geoff.right(90)

patrick = rg.SimpleTurtle('turtle')
patrick.pen = rg.Pen('blue', 30)
patrick.speed = 10

patrick.backward(20)
patrick.left(90)
patrick.forward(20)
patrick.right(90)

patrick.forward(200)
patrick.right(90)
patrick.forward(200)
patrick.right(90)
patrick.forward(400)
patrick.right(90)
patrick.forward(400)
patrick.right(90)
patrick.forward(400)
patrick.right(90)

patrick.speed = 100
geoff.speed = 100

distance = 0

for k in range(10):
    patrick.forward(distance)
    patrick.right(90)
    patrick.forward(distance)
    patrick.right(90)
    patrick.forward(distance)
    patrick.right(90)
    patrick.forward(distance)
    patrick.right(90)
    patrick.forward(distance)
    patrick.right(90)

    geoff.forward(distance)
    geoff.right(90)
    geoff.forward(distance)
    geoff.right(90)
    geoff.forward(distance)
    geoff.right(90)
    geoff.forward(distance)
    geoff.right(90)
    geoff.forward(distance)
    geoff.right(90)

    distance = distance + 11

window.close_on_mouse_click()
