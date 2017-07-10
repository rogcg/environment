#/usr/bin/env/python

from modules.galaxy.Galaxy import Galaxy
from modules.solar_system.SolarSystem import SolarSystem

print "==== ENVIRONMENT ===="

# world_name = raw_input('Enter world name: ')
# world_size = raw_input('Enter world size in km: ')

# print("%s - %s" % (world_name, world_size))

# create galaxy
galaxy = Galaxy()
galaxy.create_black_hole()

# create solar system
solar_system = SolarSystem(galaxy)