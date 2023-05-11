# ENPM661-Proj5

#Running informed_rrt_star: :
	1. launch the python file (informed_rrt_star.py) using VScode or any other similar program
	2. hit run to initiate the code (to run the current inputs)
	3. the code will run and show a simulation of the outcome
    4. inputs that can be changed in the main:
        1. start and goal points (lines 327 and 328), the code will not run if the points are not valid
        2. Number of iterations (line 326), it can be changed to exit the search at the deisred itteration number if a path was not found with the other contrains 
        3. Goal radius (line 329)
        4. rewiring radius (line 330)
        5. cbest (line 331). This is the desired cbest, this is one of the contrains the code will stop the search once its met
        6. time limit (line 332). time limit for the code to run if none of the other constains have been met
        7. map used (line 334 after mapping.) there are a couple of different maps that can be used, please see mapping.py for the options
	5. the code will run and solve for the path using informed RRT*
	6. once the path is found before hitting the time limit, the code will exit the search and display the results. 
    7. if you would like to see the cbest being optimized, you can uncomment line (62). this will show the cbest after the first solution is found until the code stops the search
	
#Running RRT*: 
	1. launch the python file (rrt_star.py) using VScode or any other similar program
	2. hit run to initiate the code (to run the current inputs)
	3. the code will run and show the outcome
    4. inputs that can be changed in the main:
        1. start and goal points (lines 275 and 276), the code will not run if the points are not valid
        2. Number of iterations (line 274), it can be changed to exit the search at the deisred itteration number if a path was not found with the other contrains 
        3. Goal radius (line 277)
        4. rewiring radius (line 278)
        5. cbest (line 279). This is the desired cbest, this is one of the contrains the code will stop the search once its met
        6. time limit (line 280). time limit for the code to run if none of the other constains have been met
        7. map used (line 282 after mapping.) there are a couple of different maps that can be used, please see mapping.py for the options
	5. the code will run and solve for the path using RRT*
	6. once the path is found before hitting the time limit, the code will exit the search and display the results. 
    7. if you would like to see the cbest being optimized, you can uncomment line (60). this will show the cbest after the first solution is found until the code stops the search
	
#libraries:
	libraries used in this project are: 
        import math
        import random
        import numpy as np
        import cv2 as cv
        import heapq
        from queue import Queue
        from heapq import heapify
        import time
        from copy import deepcopy
		
#Team Members:
	Amro Narmouq
		directory ID: narmouq7
		UID: 115405011
	Timothy Sweeny
		directory ID:tsweene1
		UID: 119359051
		
#GitHub link: 
    https://github.com/timsweeney7/ENPM661-Proj5.git	
