# rrt_star.py
import mapping
import math
import random
import numpy as np
import cv2 as cv

index = 1

start_pt = (150, 150)
pts_explored_set = set()
nodes_explored = []

#(C2C, index, parent_pt, pt_coor)
start_node = (0, 0, None, start_pt)
nodes_explored.append(start_node)


def rand_gen ():
    # generate a random x coordinate within the limit
    x_coord = random.randint(0, mapping.X_MAX_SCALED)
    # generate a random y coordinate within the limit
    y_coord = random.randint(0, mapping.Y_MAX_SCALED)

    rand_pt = (x_coord, y_coord)
    pts_explored_set.add(rand_pt)
    
    return rand_pt

def distance (pt1, pt2): 
    distance = round(math.sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2)))
    return distance

def explore (color_map): 
    global index
    index += 1
    new_pt = rand_gen ()
    if mapping.point_is_valid(color_map, new_pt):
        pts_explored_set.add(new_pt)
        dist = distance(start_pt, new_pt)
        new_node = (dist, index, start_pt, new_pt)
        nodes_explored.append(new_node)
    return nodes_explored

for i in range (0,10): 
    explore(mapping.color_map)
    

print("explored nodes:", nodes_explored)

if __name__ == "__main__":
    # print("obs_pts:", obstacle_points)
    color_map = mapping.draw_simple_map()
    cv.imshow('Informed RRT* Algorith', color_map)
    # mapping.__add_point(rand_pts)
    cv.waitKey(0)
    


print("explored nodes:", nodes_explored)
# x=rand_gen()
# # print(pts_explored)
# print(x)