import os
import sys
import subprocess
import string
import shutil

"""
MULTIBATCH - OHANA VERSION
 - for Ohana, we don't need to worry about swapping between configs.

"""

from CellModeller.Simulator import Simulator
sys.path.append('./Models')
sys.path.append('./Examples')


model_name = sys.argv[1]
num_steps = int(sys.argv[2])
num_repeats = int(sys.argv[3])
dt = float(sys.argv[4])


def simulate(mod_name, steps, dt):
    sim = Simulator(mod_name, dt)
    for i in range(num_steps):
        sim.step()

for i in range(num_repeats):
    simulate(model_name, num_steps, dt)
