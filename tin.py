import numpy as np
from scipy.spatial import Delaunay
from triangle import Triangle
from utils import *

class Tin():
    def __init__(self, points):
        self.points = points
        self.triangulation = Delaunay(np.array([(point.x, point.y) for point in points]))
        self.triangles = {}
        for coordinates in points[self.triangulation.simplices]:
            triangle = Triangle(
                coordinates[0],
                coordinates[1],
                coordinates[2]
            )
            self.triangles[str(coordinates[0]) + str(coordinates[1]) + str(coordinates[2])] = triangle
