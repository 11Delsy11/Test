import math

class point:
    def __init__(self):
        self.reset()

    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def caldist(self,other,other2):
        return math.hypot(other2.x - other.x,other2.y - other.y)
        
p1 = point()
p2 = point()
p3 = point()

p1.move(0,2)
p2.move(3**0.5,-1)


c = PointDistance()

print(c.caldist(p1,p2))

