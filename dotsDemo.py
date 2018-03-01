#Caleb Callaway
#3/1/18
#dotsDemo.py- using loops with graphics


from ggame import *

green = Color(0x00FF00,1)

dot = CircleAsset(50,LineStyle(1,green), green)


Sprite(dot,(100,100))

App().run()