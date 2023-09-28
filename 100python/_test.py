from math import sqrt
from itertools import combinations

def distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle():
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def isTriangle(self):
        x1, y1 = self.point2.x - self.point1.x, self.point2.y - self.point1.y
        x2, y2 = self.point3.x - self.point1.x, self.point3.y - self.point1.y
        
        return not(abs(x1 * y2 - x2 * y1) < 1e-12)
    
    def calculate_side(self):
        self.s12 = distance(self.point1, self.point2)
        self.s13 = distance(self.point1, self.point3)
        self.s23 = distance(self.point2, self.point3)
    
    def isIsoscelesTriangle(self):
        if not(self.isTriangle()):
            return False
        self.calculate_side()
        if len(set([self.s12, self.s13, self.s23])) != 2:
            return False
        return True

with open("./rwf/tgcan.inp", "r") as rf:
    with open("./rwf/tgcan.out", "w") as wf:
        count = 0
        N = int(rf.readline())
        points = []
        for line in rf:
            points.append(tuple(map(int,(line.split()))))

        points = [Point(x,y) for x, y in points]
        cmb_3 = [Triangle(x,y,z) for x,y,z in list(combinations(set(points), 3))]

        for tri in cmb_3:
            if tri.isIsoscelesTriangle():
                count += 1
        wf.write(str(count))