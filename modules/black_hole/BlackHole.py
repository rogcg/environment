#/usr/bin/env/python

import math

from modules.black_hole.EventHorizon import EventHorizon
import modules.__globals__ as __globals__

class BlackHole:


    '''Attributes of a non-rotating black hole
	http://hepguru.com/blackholes/characteristics.htm
    
    Event Horizon = c = (3.0E^10) (boundary of the blackhole)
	Schwarzschild Radius 
	Singularity

    * Escape velocity formula in General relativity and Newton gravity is the same
	Escape Velocity = sqrt(2GM/R)  
            G = newton's gravity constant
            M = mass of the planet
            R = separation of the planet's centre of mass (Schwarzschild Radius = Event Horizon for a non-rotating blackhole)
    '''

    event_horizon_value = 0
    escape_velocity_value = 0
    singularity_value = 0

    def __init__(self):
        event_horizon = EventHorizon()    
        self.event_horizon_value = event_horizon.calculate_event_horizon()    
        self.escape_velocity_value = self.calculate_escape_velocity(self.event_horizon_value)
        
    def calculate_escape_velocity(self, event_horizon):
        
        '''We can assume that the escape velocity at the surface is equal to the speed of light. But we need to calculate
        the increase of the escape velocity as it approaches the black hole center.'''

        # calculate the volume of the black hole. assuming the black hole is a sphere in this case, we calculate its 
        # volume using the sphere volume's formula. MAYBE IT'S A WRONG APROACH, BUT FUCK IT!
        # 4/3*pi*r^3
        # schwardzchild radius is equal to the event horizon?
        v = (4/3)*__globals__.PI*math.pow(3, event_horizon)

        # calculate newton's gravitational constant for the black hole
        m3 = float(math.pow(3, v)) # m^3
        kg1 = float(math.pow(-1, __globals__.BLACK_HOLE_MASS)) # kg^-1
        s2 = float(-math.pow(2, event_horizon*2)) # s^-2
        g = (6.67408*(-math.pow(-11, 10)))*m3*kg1*s2

        # multiply newton's gravitational constant with black hole mass defined in __globals__.py
        temp = 2 * g * __globals__.BLACK_HOLE_MASS
        # divide by the event horizon received as parameter, which is the same as the Schwarzschild Radius, since
        # we are simulating a non-rotating black hole        
        return temp/event_horizon



        