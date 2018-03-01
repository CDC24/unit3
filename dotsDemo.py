#Caleb Callaway
#3/1/18
#dotsDemo.py- using loops with graphics


from ggame import *

green = Color(0x00FF00,1)

dot = CircleAsset(25,LineStyle(1,green), green)

for i in range (1,10):
    Sprite(dot,(10i,10))

App().run()