from random import randint
import numpy as np
from point import *

def grid_to_raster(grid):
    # Map 2d array of Points to pixel values, taking interpolated value whenever available
    raster = list()
    num_inter = 0
    num_actual_value = 0
    for i in range(len(grid)):
        lst = list()
        for j in range(len(grid[i])):
            # use point interpolated_value if exists, else use value
            lst.append(grid[i][j].interpolated_value if grid[i][j].error > 0 else grid[i][j].value)
            if (grid[i][j].error > 0):
                num_inter += 1
            else:
                num_actual_value +=1
        raster.append(lst)
    total = num_inter + num_actual_value
    print("Number of interpolated pixels: ", num_inter, '({:.1%})'.format(num_inter / total))
    print("Number of actual value pixels: ", num_actual_value, '({:.1%})'.format(num_actual_value / total))
    return np.array(raster)

def raster_to_grid(raster):
    # Map 2d array of values to Points
    grid = list()
    for i in range(len(raster)):
        lst = list()
        for j in range(len(raster[i])):
            lst.append(Point(i,j, raster[i][j] if raster[i][j] > 0 else 1))
        grid.append(lst)
    return np.array(grid)

def get_grid_corners(grid):
    corners = np.array(grid[[0,0,-1,-1],[0,-1,0,-1]])
    rest = np.setdiff1d(np.array(grid.ravel()), corners)
    return corners, rest
    
def triangle_area(p, q, r):
    # find lengths for Heron's formula
    l1 = np.sqrt((p.x - q.x)**2 + (p.y - q.y)**2)
    l2 = np.sqrt((q.x - r.x)**2 + (q.y - r.y)**2)
    l3 = np.sqrt((r.x - p.x)**2 + (r.y - p.y)**2)
    p = (l1 + l2 + l3)/2
    return np.sqrt(abs(p * (p - l1) * (p - l2) * (p - l3))) # issue where sqrt of neg. value