# rrt_star.py
import mapping
import math
import random
import numpy as np
import cv2 as cv
from mapping import SCALE_FACTOR
from shapely.geometry import LineString, Point, Polygon


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
    line = LineString([pt1, pt2])
    for point in line.coords:
        point_int = tuple(map(int, point))
        if not mapping.point_is_valid(color_map=color_map, coordinates=point_int):
            distance = 5000
    return distance


    
def explore(color_map, explored_coor_local, explored_nodes_local):
    new_pt = get_random_point()
    if mapping.point_is_valid(color_map=color_map, coordinates=new_pt):
        # Find the explored point that is closest to the new point
        closest_pt = min(explored_coor_local, key=lambda pt: distance(new_pt, pt))
        if path_is_good(new_pt, closest_pt): 
            NewNode = {"c2c": distance(new_pt, closest_pt), "parentCoordinates": closest_pt, "pointCoordinates": new_pt}
        else:
            NewNode = {"c2c": 0, "parentCoordinates": (0,0), "pointCoordinates": new_pt}
        explored_nodes_local.append(NewNode)
        # mapping.__draw_line(new_pt, closest_pt, map=color_map, color=(255,255,0))
        explored_coor_local.append(new_pt)
        


if __name__ == "__main__":

    explored_coordinates = []
    Explored_Nodes = []

    color_map = mapping.draw_simple_map()
    node_info_map = create_node_info_map(color_map)
    
    starting_node_coordinates = (150*SCALE_FACTOR, 120*SCALE_FACTOR)
    starting_node = {"c2c": 0, "parentCoordinates": None, "pointCoordinates": starting_node_coordinates}
    
    Explored_Nodes.append(starting_node)
    explored_coordinates.append(starting_node_coordinates)
    
    node_info_map[starting_node_coordinates[0]] [starting_node_coordinates[1]] = starting_node

    for i in range(0, 10):
        explore(color_map=color_map, explored_coor_local=explored_coordinates, explored_nodes_local=Explored_Nodes)


    for i in Explored_Nodes:
        print(i)
    
    for i in Explored_Nodes:
        mapping.draw_node(child_coordinates=i["pointCoordinates"], \
                          parent_coordinates=i["parentCoordinates"], \
                          map= color_map, color= mapping.BLUE)

    # color_map = mapping.draw_simple_map()
    cv.imshow('Informed RRT* Algorith', color_map)
    cv.waitKey(0)
