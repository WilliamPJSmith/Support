import os
import sys
import subprocess
import string
import shutil

"""
ARGUMENTS FOR THIS SCRIPT:
1. the module name (not path) e.g ex1a_SimpleGrowth2D
2. the number of repeats
3. the path to a CM config file -- choose either:
	a. ~/cellmodeller/Config/CMconfig_PORT.cfg   		[option 0]
	b. ~/cellmodeller/Config/CMconfig_STARBOARD.cfg		[option 2]
"""

from CellModeller.Simulator import Simulator

sys.path.append('./Models')
sys.path.append('./Examples')

max_cells = 5000
num_repeats = int(sys.argv[2])

def simulate(mod_name, config_file):
    sim = Simulator(mod_name, 0.25, config_file)
    while len(sim.cellStates) < max_cells:
        sim.step()

for i in range(num_repeats):
    simulate(sys.argv[1], int(sys.argv[3]))
