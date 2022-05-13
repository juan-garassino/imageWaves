import numpy as np
import time

class Sculptor:
    def __init__(self,void_dim=12, n_planes=5, element_min_side=3, element_max_side=9, step=1, verbose=True):
        self.void_dim = void_dim
        self.void = np.zeros((self.void_dim, self.void_dim, self.void_dim))
        self.element_min_side = element_min_side
        self.element_max_side = element_max_side
        self.step = step
        self.verbose = verbose
        self.n_planes = n_planes
        

    def add_plane(self, void, axis_selection, element_min_side, element_max_side, sstep, verbose): # element sizes

        section = np.random.randint(low=0-1, high=void[0].shape[0])
        # selection of the axis to work on

        if axis_selection == 0:
            working_plane = void[section,:,:]
        elif axis_selection == 1:
            working_plane = void[:,section,:]  
        elif axis_selection == 2:
            working_plane = void[:,:,section]
        else:
            print("error")
        # axis selection

        if verbose == True:
            print(working_plane)
            print("###############################################################")

        #Variables

        element = np.ones((random.randrange(element_min_side, element_max_side, step), random.randrange(element_min_side, element_max_side, step)))
        # creates the element to be inserted
        delta = np.array(working_plane.shape) - np.array(element.shape) 
        # finds the delta between the size of the void and the size of the element
        top_left_corner = (coor_i, coor_j) = (np.random.randint(low=0, high=delta[0]) , np.random.randint(low=0, high=delta[1]))
        # finds the coordinates of the top left corner
        top_left_corner = np.array(top_left_corner)
        # converts the result in an array
        bottom_right_corner = np.array(top_left_corner) + np.array(element.shape) #- np.array([1,1]))
        # finds the coordinates of the bottom right corner
        working_plane[top_left_corner[0]:bottom_right_corner[0] , top_left_corner[1]:bottom_right_corner[1]] = element
        # makes the slides using the coordinates equal to the element

        if verbose == True:
            print(f"void shape is: {np.array(void[0].shape)}")
            print(f"element shape is : {np.array(element.shape)}")
            print(f"the axis selection is: {axis_selection}")
            print(f"delta is: {delta}")
            print(f"section is: {section}")
            print(f"top left corner is: {top_left_corner}")
            print(f"bottom right corner is: {bottom_right_corner}")
            print(f"slices are: {top_left_corner[0]}:{bottom_right_corner[0]} and {top_left_corner[1]}:{bottom_right_corner[1]}")
            print("###############################################################")

    def generative_sculpt(self):

        for i in range(self.n_planes):
            time.sleep(0.5)
            axis_selection = np.random.randint(low=0, high=3)
            add_plane(self.void, axis_selection, self.element_min_side, self.element_max_side, self.step, self.verbose)

        return self.void