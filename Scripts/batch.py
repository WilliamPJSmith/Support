import os
import sys
import subprocess
import string
import shutil

from CellModeller.Simulator import Simulator

sys.path.append('/home/gpgpu2020/cellmodeller/Models')

max_cells = 20000
cell_buffer = 256
device = 0

def simulate(mod_name, device):
    sim = Simulator(mod_name, 0.25, device)
    while len(sim.cellStates) < max_cells-cell_buffer:
        sim.step()

simulate(sys.argv[1], device)
