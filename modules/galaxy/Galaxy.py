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
    black_hole = None
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
        self.black_hole = BlackHole()         
        # Add a black hole to the center of the 3d array
        m_shape = self.galaxy_matrix.shape
        self.galaxy_matrix[m_shape[0]/2][m_shape[1]/2][m_shape[2]/2] = self.black_hole

    def create_galaxy_sectors(self):

        # Add a black hole to the center of the 3d array
        m_shape = self.galaxy_matrix.shape

        # Create  matrix inside each matrix position. (Each matrix position is equivalent to 1KPC)
        for i in range(0, m_shape[0]):
            for j in range(0, m_shape[1]):
                for k in range(0, m_shape[2]):
                    if not isinstance(self.galaxy_matrix[i][j][k], BlackHole):
                        self.galaxy_matrix[i][j][k] = np.empty((self.size, self.size, self.size), dtype=object)  
        
    def kpc_to_au(self, kpc_size):

        return kpc_size * __globals__.KPC_TO_AU

    def set_elements(self):

        for e in elements:
            print "%s %s %s" % (e.symbol, e.name, e.mass)