#/usr/bin/env/python

import random

import static_attrs
import modules.__globals__ as __globals__

from externals.periodictable import core, mass, density, elements, formula

from modules.black_hole.BlackHole import BlackHole

class Galaxy:

    typo = static_attrs.galaxy_type
    galaxy_matrix = []
    size = 0

    # Constructor
    def __init__(self):
        # Randomly intializes the size of the galaxy in KPC
        start = int((static_attrs.galaxy_size_kpc * random.random()))
        end = int(static_attrs.galaxy_size_kpc)

        # Size of the galaxy equaly on X and Y axis
        self.size = random.randint(start, end)

        # The galaxy is a matrix with the size generated before
        self.galaxy_matrix = [[0 for x in range(self.size)] for y in range(self.size)] 
        return


    def create_black_hole(self):

        print "======================"
        print "Creating a black hole."
        print "======================"
        black_hole = BlackHole()

        self.galaxy_matrix[self.size/2][self.size/2] = black_hole

        x = 0;
        y = 0;
        # Create  matrix inside each matrix position. (Each matrix position is equivalent to 1KPC)
        while x <= (len(self.galaxy_matrix)-1):
            while y <= (len(self.galaxy_matrix)-1):
                self.galaxy_matrix[x][y] = [[0 for a in range(100)] for b in range(100)]
                x += 1
                y += 1

        self.set_elements()

        print "======================"
        print ("Your galaxy has the \nsize of %d KPC which is \nequivalent to %d AU, \nand also a black hole \nin its center." % (self.size, self.kpc_to_au(self.size)))
        print "======================"

        print "======================"
        print ("Black Hole event horizon is \n %s \n and scape velocity is \n %s" % (black_hole.event_horizon_value, black_hole.escape_velocity_value)) 
        print "======================"

    def kpc_to_au(self, kpc_size):

        return kpc_size * __globals__.KPC_TO_AU

    def set_elements(self):

        for e in elements:
            print "%s %s %s" % (e.symbol, e.name, e.mass)