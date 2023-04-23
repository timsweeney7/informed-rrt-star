# rrt_star.py
import mapping
import math
import random
import numpy as np
import cv2 as cv
from mapping import SCALE_FACTOR

class Node:
    def __init__(self):
        self.costToCome = float('inf')
        self.parentCoordinates = []

    def __str__(self):
        return f"Cost To Come: {self.costToCome}  Parent Coordinates: {self.parentCoordinates}"


def create_node_info_map(color_map):
    node_info_map = np.ndarray.tolist(color_map)
    
    node_info_map[:][:] = {"c2c": float('inf'), "parentCoor": None}
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


def explore (color_map, explored_list_local): 
    new_pt = get_random_point()
    if mapping.point_is_valid(color_map=color_map, coordinates=new_pt):
        explored_list_local.append(new_pt)
        


if __name__ == "__main__":

    explored_list = []

    color_map = mapping.draw_simple_map()
    node_info_map = create_node_info_map(color_map)
    
    starting_node_coordinates = (150*SCALE_FACTOR, 150*SCALE_FACTOR)
    starting_node = {"c2c": 0, "parentCoordinates": None}
    node_info_map[starting_node_coordinates[0]] [starting_node_coordinates[1]] = starting_node

    for i in range(0, 10):
        explore(color_map=color_map, explored_list_local=explored_list)

    for i in explored_list:
        print( i)
