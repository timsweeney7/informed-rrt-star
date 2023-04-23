import heapq as hq
import copy
import numpy as np
import math
from matplotlib import pyplot as plt
import cv2 as cv
from numpy import tan, deg2rad



SCALE_FACTOR = 2

BLUE = (255, 0, 0)
DARK_GREEN = (15, 168, 33)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
YELLOW = (9, 227, 212)
BLACK = (0, 0, 0)
GRAY = (199, 198, 195)

# for coordinates
X = 0
Y = 1

# map dimensions
X_MAX = 600
Y_MAX = 250


obstacle_points = set()  # used to quickly look up if a point is in an obstacle
map_points = set()       # used to quickly look up if a point is in the map

node_index = 0


def draw_map_1():
    # Background
    background_color = BLACK
    map = np.zeros((250*SCALE_FACTOR, 600*SCALE_FACTOR, 3), np.uint8)
    map[:] = background_color

    # box 1 boundary
    pts = np.array([[(100) * SCALE_FACTOR, 0 * SCALE_FACTOR],
                    [(150) * SCALE_FACTOR, 0 * SCALE_FACTOR],
                    [(150) * SCALE_FACTOR, (100) * SCALE_FACTOR],
                    [(100) * SCALE_FACTOR, (100) * SCALE_FACTOR]],
                   np.int32)
    cv.fillPoly(map, [pts], YELLOW)

    # box 1
    pts = np.array([[100 * SCALE_FACTOR, 0 * SCALE_FACTOR],
                    [150 * SCALE_FACTOR, 0 * SCALE_FACTOR],
                    [150 * SCALE_FACTOR, 100 * SCALE_FACTOR],
                    [100 * SCALE_FACTOR, 100 * SCALE_FACTOR]],
                   np.int32)
    cv.fillPoly(map, [pts], BLUE)


    return map


def get_valid_point_map(color_map):
    valid_point_map = np.ones((250 * SCALE_FACTOR, 600 * SCALE_FACTOR), np.uint8)
    for x in range(0, 600 * SCALE_FACTOR):
        for y in range(0, 250 * SCALE_FACTOR):
            pixel_color = tuple(color_map[y, x])
            if pixel_color == YELLOW or pixel_color == BLUE:
                valid_point_map[y, x] = 0
    return valid_point_map


def determine_valid_point(valid_point_map, coordinates):
    if not __point_is_inside_map(coordinates[X], coordinates[Y]):
        return False
    if valid_point_map[coordinates[Y], coordinates[X]] == 1:
        return True
    else:
        return False


def __point_is_inside_map(x, y):
    if (x > 600) or (x < 0):
        return False
    elif (y > 250) or (y < 0):
        return False
    else:
        return True

def __add_point(x, y, map, color):
    map[y, x] = color
    return map


def __draw_line(p1, p2, map, color):
    pts = np.array([[p1[0], p1[1]], [p2[0], p2[1]]],
                   np.int32)
    cv.fillPoly(map, [pts], color)


def draw_node(child_coordinates, parent_coordinates, map, color):

    child_coordinates = tuple(int(SCALE_FACTOR * _) for _ in child_coordinates)
    cv.circle(map, child_coordinates, radius=3, color=color, thickness=-1)

    if (parent_coordinates is not None):
        parent_coordinates = tuple(int(SCALE_FACTOR * _ ) for _ in parent_coordinates)
        cv.circle(map, parent_coordinates, radius=3, color=color, thickness=-1)
        __draw_line(child_coordinates, parent_coordinates, map, color)
