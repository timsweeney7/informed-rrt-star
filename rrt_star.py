# rrt_star.py
import mapping
import math
import random
import numpy as np
import cv2 as cv

X_MAX = 300
Y_MAX = 300
index = 1

start_pt = (150, 150)
pts_explored_set = set()
nodes_explored = []


class Node:
    def __init__(self):
        self.costToCome = float('inf')
        self.parentCoordinates = []

    def __str__(self):
        return f"Cost To Come: {self.costToCome}  Parent Coordinates: {self.parentCoordinates}"


def create_node_info_map(color_map):
    node_info_map = np.ndarray.tolist(color_map)
    
    node_info_map[:][:] = {"c2c": 10, "parentCoor": (10,10)}
    return node_info_map


def get_random_point ():
    # generate a random x coordinate within the limit
    x_coord = random.randint(0, mapping.X_MAX_SCALED)
    # generate a random y coordinate within the limit
    y_coord = random.randint(0, mapping.Y_MAX_SCALED)
    rand_pt = (x_coord, y_coord)
    return rand_pt
    

def distance (pt1, pt2): 
    distance = round(math.sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2)))
    return distance


def explore (color_map): 
    new_pt = get_random_point()
    if mapping.point_is_valid(color_map=color_map, coordinates=new_pt):
        c2c = distance(start_pt, new_pt)
        parentCoor = [0,0]
        new_node = Node()
        new_node.costToCome = c2c
        new_node.parentCoordinates = parentCoor
        nodes_explored.append(new_node)
        return nodes_explored


if __name__ == "__main__":

    color_map = mapping.draw_simple_map()
    node_info_map = create_node_info_map(color_map)
    #cv.imshow('Informed RRT* Algorithm', color_map)
    #cv.waitKey(0)
