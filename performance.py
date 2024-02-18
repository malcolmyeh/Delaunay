import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from Delaunay import MyDelaunay
import time
from utils import *
from Fjallstrom import *
import cv2

# n_lst = []
# scipy_performance = []
# my_delaunay_performance = []

# for n in range(10, 150):
#     print(n, end='\r')
#     n_lst.append(n)
#     points = np.random.random((n, 2))
#     start = time.time()
#     Delaunay(points)
#     end = time.time()
#     scipy_performance.append(end - start)
#     start = time.time()
#     MyDelaunay(points)
#     end = time.time()
#     my_delaunay_performance.append(end - start)

# plt.plot(n_lst, scipy_performance, label="SciPy")
# plt.plot(n_lst, my_delaunay_performance, label="Bowyer-Watson")
# plt.xlabel("Points")
# plt.ylabel("Time")
# plt.legend(loc='best')
# plt.show()

# n_lst = []
# fjallstrom_performance = []
# for n in range(5, 30):
#     n_lst.append(n)
#     raster = generate_raster(n);
#     grid = raster_to_grid(raster)
#     start = time.time()
#     fjallstrom(grid, 0.5)
#     end = time.time()
#     fjallstrom_performance.append(end - start)
# plt.plot(n_lst, fjallstrom_performance, label="Fjallstrom")
# plt.xlabel("Size")
# plt.ylabel("Time")
# plt.legend(loc='best')
# plt.show()

# n_lst = []
# fjallstrom_performance = []
# for n in range(5, 30):
#     n_lst.append(n)
#     raster = generate_raster(n);
#     grid = raster_to_grid(raster)
#     start = time.time()
#     fjallstrom(grid, 0.5)
#     end = time.time()
#     fjallstrom_performance.append(end - start)
# plt.plot(n_lst, fjallstrom_performance, label="Fjallstrom")
# plt.xlabel("Size")
# plt.ylabel("Time")
# plt.legend(loc='best')
# plt.show()


# n_list = []
# fjallstrom_performance = []
# image = cv2.imread("30x30_4.png")
# raster = np.array(image)
# raster = cv2.cvtColor(raster, cv2.COLOR_BGR2GRAY)
# grid = raster_to_grid(raster)
# for n in range(1, 9):
#     f = n/10
#     n_lst.append(f)
#     start = time.time()
#     fjallstrom(grid, f)
#     end = time.time()
#     fjallstrom_performance.append(end - start)

# plt.plot(n_lst, fjallstrom_performance, label="Fjallstrom")
# plt.xlabel("Error")
# plt.ylabel("Time")
# plt.legend(loc='best')
# plt.show()
