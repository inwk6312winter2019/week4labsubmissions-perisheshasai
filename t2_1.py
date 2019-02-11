from math import *
class point:
        def __init__(self,x,y):
                self.x=x
                self.y=y
class rectangle:
        def __init__(self,width,height):
                self.width=width
                self.height=height
                self.corner=(x1.x,x1.y)
def move_rectangle():
        x1.x= x1.x+dx
        x1.y= x1.y+dy
        print ("moved recatngle= ",x1.x, x1.y)
x1=point(0,0)
print ("origin =","(",x1.x,",",x1.y,")")
dx=9
dy=4
move_rectangle()
