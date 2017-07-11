#/usr/bin/env/python

import random

import numpy as np

import static_attrs
import modules.__globals__ as __globals__

from externals.periodictable import core, mass, density, elements, formula

from modules.black_hole.BlackHole import BlackHole

class Galaxy:

    typo = static_attrs.galaxy_type
    galaxy_matrix = None
    size = 0

    # Constructor
    def __init__(self, size_):
        
        self.size = size_
        self.galaxy_matrix = np.empty((self.size, self.size, self.size), dtype=object)    
        return


    def create_black_hole(self):

        print "======================"
        print "Creating a black hole."
        print "======================"
        black_hole = BlackHole()

        # Add a black hole to the center of the 3d array
        m_shape = self.galaxy_matrix.shape
        self.galaxy_matrix[m_shape[0]/2][m_shape[1]/2][m_shape[2]/2] = black_hole

        x = 0;
        y = 0;
        # Create  matrix inside each matrix position. (Each matrix position is equivalent to 1KPC)
        for i in range(0, m_shape[0]):
            for j in range(0, m_shape[1]):
                for k in range(0, m_shape[2]):
                    if not isinstance(self.galaxy_matrix[i][j][k], BlackHole):
                        self.galaxy_matrix[i][j][k] = np.empty((self.size, self.size, self.size), dtype=object)  
         

        print self.galaxy_matrix[m_shape[0]/2][m_shape[1]/2][m_shape[2]/2] 

        #self.set_elements()

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