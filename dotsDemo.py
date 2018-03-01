#Caleb Callaway
#3/1/18
#dotsDemo.py- using loops with graphics


from ggame import *

RADIUS = 10        #capitals indicate a constant

green = Color(0x00FF00,1)

dot = CircleAsset(RADIUS,LineStyle(1,green), green)



for i in range (1,10): #puts a row aross the top
    for l in range (1,10):# puts columns
        Sprite(dot,(100*i,100*l))

App().run()