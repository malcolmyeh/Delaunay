import numpy as np
from tin import Tin
from utils import *

def fjallstrom(grid, err):
    # start with corners of grid in set S, put all other pixels as points in a set P
    points, rest = get_grid_corners(grid)

    # compute Delaunay Triangulation of S
    tin = Tin(points)

    # distribute points of P in the triangles
    distribute(tin, rest)

    error_points = np.sort(rest)

    # metrics
    original_size = error_points.size
    num_iterations = 0

    while error_points.size > 0:
        status =(original_size - error_points.size) / original_size
        print('{:.1%}'.format(status), end='\r')
        num_iterations += 1

        # find point of P that has biggest error. If small enough, stop
        biggest_error_point, error_points = error_points[-1], error_points[:-1]
        if biggest_error_point.error < err:
            print("Largest error is small enough:", biggest_error_point.error)
            break

        # otherwise, remove point from P
        rest = np.setdiff1d(rest, np.array(biggest_error_point))
        biggest_error_point.error = 0

        # add to S
        points = np.append(points, [biggest_error_point])
        
        # update Delaunay Triangulation of S
        tin = Tin(points)
        
        distribute(tin, rest)
        error_points = np.sort(rest)

    print("Fjallstrom algorithm completed in", num_iterations, "iterations. ")
    print("Number of triangles in triangulation:", len(tin.triangles))
    return tin

def distribute(tin, points):
    for point in points:
        np_points = np.array((point.x, point.y))
        # find triangle corresponding to point
        coordinates = tin.points[tin.triangulation.simplices[tin.triangulation.find_simplex(np_points)]]
        triangle = tin.triangles[str(coordinates[0]) + str(coordinates[1]) + str(coordinates[2])]

        # calculate error from interpolating point in triangle
        # find weighting
        # https://codeplea.com/triangular-interpolation
        p = triangle.p
        q = triangle.q
        r = triangle.r
        total_area = triangle_area(p,q,r)
        point.set_interpolated_value( (triangle_area(point, p, q) / total_area * r.value ) + ( triangle_area(point, q, r) / total_area * p.value ) + ( triangle_area(point, r, p) / total_area ))