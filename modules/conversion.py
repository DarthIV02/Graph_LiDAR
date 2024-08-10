import numpy as np
from sklearn.neighbors import KDTree

class Graph:
    def __init__(nodes):
        pass

    def point_to_graph_distance(points, radius): # Expects points to be x,y,z
        kdt = KDTree(points, leaf_size=10)
        ind = kdt.query_radius(points[:], r=radius)
        return ind

    def point_to_graph_knn(points, knn): # Expects points to be x,y,z
        kdt = KDTree(points, leaf_size=10)
        dist, ind = kdt.query(points, k=knn)
        return dist, ind

        