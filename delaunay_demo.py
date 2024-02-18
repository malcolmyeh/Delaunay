import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from Delaunay import MyDelaunay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", type=int, help="number of points to generate", default=10)
args = parser.parse_args()

n = args.s
print("Generating ", n, " points. ")

points = np.random.random((n, 2))
print("points:\n", points)
dt = MyDelaunay(points)
dt2 = Delaunay(points)
print("Delaunay triangles:\n", dt.simplices)
print("Scipy triangles:\n", dt2.simplices)

plt.figure()
plt.title("SciPy Implementation")
plt.triplot(points[:,0], points[:,1], dt2.simplices)
plt.plot(points[:,0], points[:,1], 'o')

plt.figure()
plt.title("Bowyer-Watson")
plt.triplot(points[:,0], points[:,1], dt.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()