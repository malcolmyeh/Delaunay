import numpy as np

class Triangle(object):
    def __init__(self, p, q, r):
        # Vertices
        self.p = p
        self.q = q
        self.r = r
        self.edges = [[self.p, self.q],
                        [self,p,self,r],
                        [self,q,self.r]]
        # Fjallstrom: the points from set S (midpoints of grid cells) that fall within the triangle
        self.points = np.array([])

    def add_points(self, points):
        self.points.append(points)
    def tostring(self):
        return 't(' + str(self.p) + ', ' + str(self.q) + ', ' + str(self.r) + ')'