#/usr/bin/env/python

import random
import static_attrs

class Galaxy:

    typo = static_attrs.galaxy_type
    size = 0

    # Constructor
    def __init__(self):

    	# Randomly intializes the size of the galaxy in AU
    	start = int((static_attrs.galaxy_size_au * random.random()))
    	end = int(static_attrs.galaxy_size_au)

        size = random.randint(start, end)

        # The galaxy is a matrix with the size generated before
        galaxy_matrix = [[0 for x in range(size)] for y in range(size)] 

        print galaxy_matrix