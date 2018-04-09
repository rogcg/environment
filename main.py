#/usr/bin/env/python

import random

from modules.galaxy.Galaxy import Galaxy
from modules.solar_system.SolarSystem import SolarSystem

from modules.galaxy import static_attrs
import modules.__globals__ as __globals__

print "==== ENVIRONMENT ===="

# world_name = raw_input('Enter world name: ')
# world_size = raw_input('Enter world size in km: ')

# print("%s - %s" % (world_name, world_size))

# create galaxy
# Randomly intializes the size of the galaxy in KPC
start = int((static_attrs.galaxy_size_kpc * random.random()))
end = int(static_attrs.galaxy_size_kpc)
# Size of the galaxy equaly on X, Y and Z axis
size = random.randint(start, end)

galaxy = Galaxy(size)
galaxy.create_black_hole()
galaxy.create_galaxy_sectors()

print "======================"
print ("Your galaxy has the \nsize of %d KPC which is \nequivalent to %d AU, \nand also a black hole \nin its center." % (galaxy.size, galaxy.kpc_to_au(galaxy.size)))
print "======================"

print "======================"
print ("Black Hole event horizon is \n %s \n and scape velocity is \n %s" % (galaxy.black_hole.event_horizon_value, galaxy.black_hole.escape_velocity_value)) 
print "======================"

# create solar system
#solar_system = SolarSystem(galaxy)