# rrt_star.py
import mapping
import math
import random
import numpy as np
import cv2 as cv
from mapping import SCALE_FACTOR
import heapq
from heapq import heapify



class Node:
    def __init__(self):
        self.costToCome = float('inf')
        self.parentCoordinates = []

    def __str__(self):
        return f"Cost To Come: {self.costToCome}  Parent Coordinates: {self.parentCoordinates}"


def create_pixel_info_map(color_map):
    pixel_info_map = np.ndarray.tolist(color_map)

    y_dim_len = color_map.shape[0]
    x_dim_len = color_map.shape[1]

    for x in range(0, x_dim_len):
        for y in range(0, y_dim_len):
            if mapping.point_is_valid(color_map=color_map, coordinates=(x, y)):
                obs = False
            else:
                obs = True
            pixel_info_map[y][x] = {"c2c": float('inf'), "parentCoor": None, "selfCoordinates":(x, y),"obstacle":obs}
    return pixel_info_map


def get_random_point ():
    # generate a random x coordinate within the limit
    x_coord = random.randint(0, mapping.X_MAX_SCALED-1)
    # generate a random y coordinate within the limit
    y_coord = random.randint(0, mapping.Y_MAX_SCALED-1)
    rand_pt = (x_coord, y_coord)
    return rand_pt
    

def distance (pt1, pt2): 
    distance = round(math.sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2)))
    return distance


def path_is_good(pt1, pt2):
    line = get_line_coordinates(pt1, pt2)
    for point in line:
        point_int = tuple(map(int, point))
        if not mapping.point_is_valid(color_map=color_map, coordinates=point_int):
            return False
    return True


"""
    Returns a list of coordinates between two points (x1, y1) and (x2, y2) using Bresenham's line algorithm.
"""
def get_line_coordinates(p1, p2):
    
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]

    coordinates = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy

    while x1 != x2 or y1 != y2:
        coordinates.append((x1, y1))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    coordinates.append((x2, y2))

    return coordinates


def find_closest_point(pt, explored_nodes):
    p_queue = []
    for node in explored_nodes:
        # print(node)
        dist = distance(pt, node["selfCoordinates"])
        tempC2C = dist + node["c2c"]
        # temp_node = (tempC2C, node)
        # temp_node = {"c2c": tempC2C, "parentCoordinates": node["selfCoordinates"], "selfCoordinates": pt, "obstacle": False}
        heapq.heappush(p_queue, (tempC2C, node["selfCoordinates"]))
        

    try:
        while(True):
            weight, closest_neighbor = heapq.heappop(p_queue)
            if path_is_good(pt1= pt, pt2= closest_neighbor):
                return closest_neighbor, weight
    except IndexError:
        return(None)

    
def explore(pixel_map:list, explored_nodes:list, goal_point:tuple, goal_radius):
    for i in range(0, 1000):
        new_pt = get_random_point()
        x, y = new_pt 
        if new_pt not in gen_pts_set:
            gen_pts_set.add((new_pt[0], new_pt[1]))
            if pixel_map[y][x]["obstacle"] == False:
                # Find the explored point that is closest to the new point
                closest_point = find_closest_point(new_pt, explored_nodes)
                if closest_point is not None:
                    new_node = {"c2c": closest_point[1], "parentCoordinates": closest_point[0], "selfCoordinates": new_pt, "obstacle": False}
                    # new_node = closest_point
                    explored_nodes.append(new_node)
                    pixel_map[y][x] = new_node
                    
                    #if distance(pt1= new_pt , pt2= goal_point) < goal_radius:
                    #    solution_list = backtrack(explored_nodes)
                    #    return solution_list
                    


if __name__ == "__main__":

    explored_nodes_list = []
    gen_pts_set = set()

    color_map = mapping.draw_simple_map()
    pixel_info_map = create_pixel_info_map(color_map)
    
    starting_node_coordinates = (150*SCALE_FACTOR, 120*SCALE_FACTOR)
    if( not mapping.point_is_valid(color_map=color_map, coordinates=starting_node_coordinates)):
        print("invalid starting point")
        exit()
    
    starting_node = {"c2c": 0, "parentCoordinates": None, "selfCoordinates": starting_node_coordinates, "obstacle": False, }
    explored_nodes_list.append(starting_node)
    
    pixel_info_map[starting_node["selfCoordinates"][1]] [starting_node["selfCoordinates"][0]] = starting_node


    # ------------------------------
    explore(pixel_map= pixel_info_map, explored_nodes= explored_nodes_list, goal_point=(0,0), goal_radius=0)



    #--------------------------------
    for i in explored_nodes_list:
        print(i)

    for i in explored_nodes_list:
        mapping.draw_node(child_coordinates=i["selfCoordinates"], \
                          parent_coordinates=i["parentCoordinates"], \
                          map= color_map, color= mapping.BLUE)
    cv.imshow('Informed RRT* Algorith', color_map)
    cv.waitKey(0)
    print("Explored_nodes_matrix:", len(explored_nodes_list))
    
