#/usr/bin/env/python

import math
import modules.__globals__ as __globals__

'''
Event Horizon is the area surrounding a black hole where the escape velocity is equal to the speed of light. 

The event horizon can be thought of as a massive sphere. In fact, you can think of this sphere as the "surface" 
of the black hole, although the black hole's mass all lies well within this "surface". In fact, the distance 
from Singularity to the event horizon is the Schwarzschild Radius.

1. The penrose diagram <---- ??
'''
class EventHorizon:

    # where dafuq did i found this value? it makes no sense.
	constant_force_gravity = 1.648433988

    # Mass of the black hole in KG
	black_hole_mass = __globals__.BLACK_HOLE_MASS	

	def calculate_event_horizon(self):

		"""As we simulate a non-rotating black hole, the formula for calculating the event horizon
		is the same as Schartzchild Radius formula."""

		return (2 * (self.constant_force_gravity * self.black_hole_mass)/math.pow(2, __globals__.LIGHT_SPEED))