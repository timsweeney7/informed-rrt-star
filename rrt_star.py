"""
code based on this paper:
https://arxiv.org/pdf/1105.1186.pdf
"""

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
    # calculatle c2c to pt through every node in explored_nodes
    for node in explored_nodes:
        dist = distance(pt, node["selfCoordinates"])
        tempC2C = dist + node["c2c"]
        # add the old nodes to a priority queue based on which one produces the lowest c2c
        heapq.heappush(p_queue, (tempC2C, node["selfCoordinates"]))     
    try:
        while(True):
            # pop nodes off the priority queue and check that there are no obstacles in between
            weight, closest_neighbor = heapq.heappop(p_queue)
            if path_is_good(pt1= pt, pt2= closest_neighbor):
                return {"c2c_plus_dist": weight, "coordinates": closest_neighbor}
    except IndexError:
        return(None)

    
def explore(pixel_map:list, explored_nodes:list, goal_point:tuple, goal_radius, num_of_iterations:int):
    gen_pts_set = set()
    for i in range(0, num_of_iterations):
        new_pt = get_random_point()
        x, y = new_pt 
        if new_pt not in gen_pts_set:
            gen_pts_set.add((new_pt[0], new_pt[1]))
            if pixel_map[y][x]["obstacle"] == False:
                # Find the explored point that is closest to the new point
                closest_point = find_closest_point(new_pt, explored_nodes)
                if closest_point is not None:
                    new_node = {"c2c": closest_point["c2c_plus_dist"], \
                                "parentCoordinates": closest_point["coordinates"], \
                                "selfCoordinates": new_pt, \
                                "obstacle": False}
                    explored_nodes.append(new_node)
                    pixel_map[y][x] = new_node
                    
                    if distance(pt1= new_pt , pt2= goal_point) < goal_radius:
                        return True  # return 0 if a solution is found
    # return 1 if no solution is found
    return False
                    

def backtrack (explored_nodes:list, map_:list):
    print("Backtracking...")
    solution_path = []
    current_node = explored_nodes[-1]
    solution_path.append(current_node)
    
    # (C2G, C2C, TC, point_index, (x,y,theta)parent_coordinates, (x,y,theta)coordinates)
    while current_node["parentCoordinates"] is not None:
        x, y = current_node["parentCoordinates"]
        parent_node = map_[y][x]
        current_node = parent_node
        solution_path.append(parent_node)

    solution_path.reverse()
    return solution_path 



if __name__ == "__main__":

    # --- Simulation Setup -----------------------
    explored_nodes_list = []
    NUM_OF_ITERATIONS = 5000
    START_POINT = (150, 120)
    GOAL_POINT = (290, 290)
    GOAL_RADIUS = 5

    color_map = mapping.draw_simple_map()
    pixel_info_map = create_pixel_info_map(color_map)
    
    if( not mapping.point_is_valid(color_map=color_map, coordinates=START_POINT)):
        print("invalid starting point")
        exit()

    if( not mapping.point_is_valid(color_map=color_map, coordinates=GOAL_POINT)):
        print("invalid goal point")
        exit()
    
    starting_node = {"c2c": 0, "parentCoordinates": None, "selfCoordinates": START_POINT, "obstacle": False}
    explored_nodes_list.append(starting_node)
    
    pixel_info_map[starting_node["selfCoordinates"][1]] [starting_node["selfCoordinates"][0]] = starting_node

    
    # --- Run the algorithm ---------------------------
    solution_found = explore(pixel_map= pixel_info_map, \
                             explored_nodes= explored_nodes_list, \
                             goal_point=GOAL_POINT,\
                             goal_radius=GOAL_RADIUS, \
                             num_of_iterations= NUM_OF_ITERATIONS)
    if solution_found == True:
        print("Number of iterations needed to find solution: " + str(len(explored_nodes_list)))
        solution = backtrack(explored_nodes= explored_nodes_list, map_= pixel_info_map)
    else: 
        print("Solution not found after " + str(NUM_OF_ITERATIONS) + " points checked!")
        exit()


    #--- Display results ----------------------------

    for i in explored_nodes_list:
        mapping.draw_node(child_coordinates=i["selfCoordinates"], \
                          parent_coordinates=i["parentCoordinates"], \
                          map= color_map, color= mapping.BLUE)
    cv.imshow('RRT* Algorithm', color_map)
    cv.waitKey(0)

    cv.circle(color_map, GOAL_POINT, radius=GOAL_RADIUS, color=mapping.GRAY, thickness=-1)

    for i in solution:
        mapping.draw_node(child_coordinates=i["selfCoordinates"], \
                          parent_coordinates=i["parentCoordinates"], \
                          map= color_map, color= mapping.RED)
        cv.imshow('RRT* Algorithm', color_map)
        cv.waitKey(0)
                        
    end_point = solution[-1]
    mapping.draw_node(child_coordinates=i["selfCoordinates"], \
                      parent_coordinates= None, \
                      map= color_map, color= mapping.GREEN)
    cv.imshow('RRT* Algorithm', color_map)
    cv.waitKey(0)

    print("Explored_nodes_matrix:", len(explored_nodes_list))
    
