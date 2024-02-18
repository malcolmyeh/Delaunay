import numpy as np

class MyDelaunay:
    def __init__(self, points):
        # https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

        # Initial coordinates for corners
        self.coordinates = [np.array((-1000,-1000)), np.array((1000,-1000)), np.array((1000,1000)), np.array((-1000,1000))]

        # key is the indices of the three points that make up the triangle inside the coordinates list
        # values are triangles that are share the vertice (neighbour)
        self.triangles = {}

        # Create two super triangles from corners coordinate indexes so that all points will be enclosed
        """
        *⎻⎻⎻⎻*
        |\ 2 |
        | \  |
        |  \ |
        | 1 \|
        *⎻⎻⎻⎻*
        """
        super_triangle_1 = (0, 1, 3)
        super_triangle_2 = (2, 3, 1)
        self.triangles[super_triangle_1] = [super_triangle_2, None, None]
        self.triangles[super_triangle_2] = [super_triangle_1, None, None]


        # Add all the points one at a time to the triangulation
        for p in points:
            p = np.asarray(p)
            idx = len(self.coordinates)
            self.coordinates.append(p)

            # First find all the triangles that are no longer valid due to the insertion
            bad_triangles = []
            for triangle in self.triangles:
                if self.isPointInCircumcircle(triangle, p):
                    bad_triangles.append(triangle)

            # Find the boundary of the polygonal hole
            # Store edges and triangle that shares edge
            polygon = []

            # find bad triangles that share edge starting with the first bad triangle to find polygon
            bad_triangle = bad_triangles[0]
            edge = 0
            while True:
                shared_triangle = self.triangles[bad_triangle][edge]
                if shared_triangle not in bad_triangles:
                    next_edge = (edge+1) % 3
                    prev_edge = (edge-1) % 3
                    polygon.append((bad_triangle[next_edge], bad_triangle[prev_edge], shared_triangle))
                    edge = next_edge
                    if polygon[0][0] == polygon[-1][1]:
                        break
                else:
                    edge = (self.triangles[shared_triangle].index(bad_triangle) + 1) % 3
                    bad_triangle = shared_triangle

            # remove them from the data structure
            for bad_triangle in bad_triangles:
                del self.triangles[bad_triangle]

            # re-triangulate the polygonal hole
            new_triangles = []
            for (edge_start, edge_end, shared_triangle) in polygon:

                # form new triangle using edges
                new_triangle = (idx, edge_start, )

                # add to triangle dictionary 
                self.triangles[new_triangle] = [shared_triangle, None, None]

                # set new_triangle as neighbour of shared_triangle
                if shared_triangle:
                    for i in range(len(self.triangles[shared_triangle])):
                        neighbour = self.triangles[shared_triangle][i]
                        if neighbour and edge_start in neighbour and edge_end in neighbour:
                            self.triangles[shared_triangle][i] = new_triangle
                new_triangles.append(new_triangle)

            # set new_triangles as neighbours
            for i in range(len(new_triangles)):
                next_triangle_index = (i+1) % len(new_triangles)
                prev_triangle_index = (i-1) % len(new_triangles)
                self.triangles[new_triangles[i]][1] = new_triangles[next_triangle_index]
                self.triangles[new_triangles[i]][2] = new_triangles[prev_triangle_index]

        # set simplices to triangles with vertexes within bounds (exclude triangles that touch initial corner points)
        valid_triangles = [[a,b,c] for (a,b,c) in self.triangles if a > 3 and b > 3 and c > 3]

        # shift triangle indexes down by 4
        for valid_triangle in valid_triangles:
            valid_triangle[0] = valid_triangle[0] - 4
            valid_triangle[1] = valid_triangle[1] - 4
            valid_triangle[2] = valid_triangle[2] - 4

        self.simplices = np.array(valid_triangles)

    def isPointInCircumcircle(self, triangle, point):
        # calculate circumcircle of triangle and determine whether point lies within it
        # https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcenter_coordinates

        points = np.asarray([self.coordinates[vertex] for vertex in triangle])
        d = ( (points[0][0] - points[2][0]) * (points[1][1] - points[2][1]) - (points[1][0] -  points[2][0]) * (points[0][1] - points[2][1]) )
        u_x = (((points[0][0] - points[2][0]) * (points[0][0] + points[2][0]) + (points[0][1] - points[2][1]) * (points[0][1] + points[2][1])) / 2 * (points[1][1] - points[2][1]) - ((points[1][0] - points[2][0]) * (points[1][0] + points[2][0]) + (points[1][1] - points[2][1]) * (points[1][1] + points[2][1])) / 2 * (points[0][1] - points[2][1])) / d
        u_y = (((points[1][0] - points[2][0]) * (points[1][0] + points[2][0]) + (points[1][1] - points[2][1]) * (points[1][1] + points[2][1])) / 2 * (points[0][0] - points[2][0]) - ((points[0][0] - points[2][0]) * (points[0][0] + points[2][0]) + (points[0][1] - points[2][1]) * (points[0][1] + points[2][1])) / 2 * (points[1][0] - points[2][0])) / d
        center = np.array((u_x, u_y))
        radius = np.sum(np.square(points[0] - center))
        return np.sum(np.square(center - point)) <= radius