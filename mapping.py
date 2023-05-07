import numpy as np
import cv2 as cv
import random


# map dimensions
X_MAX = 300
Y_MAX = 300
SCALE_FACTOR = 1
X_MAX_SCALED = X_MAX * SCALE_FACTOR
Y_MAX_SCALED = Y_MAX * SCALE_FACTOR
Half_X_Max = int(X_MAX/2)
Half_Y_Max = int(Y_MAX/2)

BLUE = (255, 0, 0)
DARK_GREEN = (15, 168, 33)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
YELLOW = (9, 227, 212)
BLACK = (0, 0, 0)
GRAY = (199, 198, 195)
WHITE = (255,255,255)

# for coordinates
X = 0
Y = 1

def draw_simple_map():
    background_color = WHITE
    map = np.zeros((Y_MAX_SCALED, X_MAX_SCALED, 3), np.uint8)
    map[:] = background_color

    # block 1
    first_point = ((Half_X_Max-25) * SCALE_FACTOR, (Half_Y_Max-25)* SCALE_FACTOR)
    second_point = ((Half_X_Max+25), (Half_Y_Max+25)* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    return map

def draw_simple_map1():
    background_color = WHITE
    map = np.zeros((Y_MAX_SCALED, X_MAX_SCALED, 3), np.uint8)
    map[:] = background_color

    # block 1
    first_point = (50 * SCALE_FACTOR, 25* SCALE_FACTOR)
    second_point = (100* SCALE_FACTOR, 75* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    # block 2
    first_point = (20* SCALE_FACTOR, 100* SCALE_FACTOR)
    second_point = (35* SCALE_FACTOR, 150* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    # block 3
    first_point = (135* SCALE_FACTOR, 140* SCALE_FACTOR)
    second_point = (165* SCALE_FACTOR, 190* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    # block 4
    first_point = (175* SCALE_FACTOR, 30* SCALE_FACTOR)
    second_point = (210* SCALE_FACTOR, 60* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    # block 5
    first_point = (250* SCALE_FACTOR, 150* SCALE_FACTOR)
    second_point = (275* SCALE_FACTOR, 185* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    # block 6
    first_point = (100 * SCALE_FACTOR, 225 * SCALE_FACTOR)
    second_point = (200 * SCALE_FACTOR, 270 * SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    return map

def draw_simple_map2():
    background_color = WHITE
    map = np.zeros((Y_MAX_SCALED, X_MAX_SCALED, 3), np.uint8)
    map[:] = background_color

    # block 1
    first_point = ((Half_X_Max-25) * SCALE_FACTOR, (Half_Y_Max-50) * SCALE_FACTOR)
    second_point = ((Half_X_Max+25) * SCALE_FACTOR, (Half_Y_Max-1) * SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    # block 2
    first_point = ((Half_X_Max-25), (Half_Y_Max+1)* SCALE_FACTOR)
    second_point = ((Half_X_Max+25), (Half_Y_Max+50)* SCALE_FACTOR)
    cv.rectangle(map, first_point, second_point, BLACK, -1)

    return map

def draw_random_map(num_of_rectangles):
    # Background
    background_color = WHITE
    map = np.zeros((Y_MAX_SCALED, X_MAX_SCALED, 3), np.uint8)
    map[:] = background_color

    for i in range(0,num_of_rectangles):
        first_point_x = random.randint(0, X_MAX_SCALED)
        first_point_y = random.randint(0, Y_MAX_SCALED)
        first_point = [first_point_x, first_point_y]
        x_increase = random.randint(10,20)
        y_increase = random.randint(10,20)
        x_increase_scaled = x_increase * SCALE_FACTOR
        y_increase_scaled = y_increase * SCALE_FACTOR
        second_point = [first_point_x + x_increase_scaled, first_point_y + y_increase_scaled]
        if second_point[1] > X_MAX_SCALED:
            second_point[1] = X_MAX_SCALED
        if second_point[0] > Y_MAX_SCALED:
            second_point[0] = Y_MAX_SCALED

        cv.rectangle(map, first_point, second_point, BLACK, -1)

    return map

"""
point_is_valid

Determines if a given set of coordinates is in free space or in obstacle space

color_map:   numpy_array of a color map. map is 3 dimensions [y, x, [color]]
coordinates: set of xy coordinates [x, y]

"""
def point_is_valid(color_map, coordinates):
    if not __point_is_inside_map(coordinates[X], coordinates[Y]):
        return False
    pixel_color = tuple(color_map[coordinates[Y], coordinates[X]])
    if pixel_color == WHITE:
        return True
    elif pixel_color == BLACK:
        return False
    else:
        raise Exception("determine_valid_point was passed an invalid argument")


def __point_is_inside_map(x, y):
    if (x > X_MAX_SCALED) or (x < 0):
        return False
    elif (y > Y_MAX_SCALED) or (y < 0):
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


if __name__ == "__main__":
    color_map = draw_simple_map2()
    cv.imshow('Informed RRT* Algorith', color_map)
    cv.waitKey(0)