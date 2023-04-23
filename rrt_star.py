# rrt_star.py
import system
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

#(C2C, index, parent_pt, pt_coor)
start_node = (0, 0, None, start_pt)
nodes_explored.append(start_node)


class Node:
    def __init__(self):
        self.costToCome = float('inf')
        self.parentCoordinates = []

    def __str__(self):
        return f"Cost To Come: {self.costToCome}  Parent Coordinates: {self.parentCoordinates}"


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


def explore (): 
    new_pt = get_random_point()
    if mapping.point_is_valid(new_pt):
        dist = distance(start_pt, new_pt)
        new_node = (dist, index, start_pt, new_pt)
        nodes_explored.append(new_node)
        return nodes_explored

if __name__ == "__main__":
    # print("obs_pts:", obstacle_points)
    #color_map = mapping.draw_simple_map()
    #cv.imshow('Informed RRT* Algorithm', color_map)
    #cv.waitKey(0)

    testNode_1 = Node()
    testNode_2 = Node()
    testNode_1.costToCome = 10
    testNode_2.costToCome = 50
    
    print(testNode_1)
    print(testNode_2)

    print() 

    for i in range (0,10): 
        explore()
    

    print("explored nodes:", nodes_explored)

    

    # x=rand_gen()
    # # print(pts_explored)
    # print(x)