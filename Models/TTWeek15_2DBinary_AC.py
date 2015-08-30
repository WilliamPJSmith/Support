import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy
import math

# fixed radius analogue of punnet square binary experiments
radius = 0.48

# specify initial volumes (different for each type)
initialVola = 0.54
initialVolb = 0.81
initialVolc = 1.16
initialVold = 1.85

# specify intial lengths
# actually, to make sure the cells begin with the same volume, we'll initiate both cells with the length of the type a cell
# (the smallest possible birth lenght). Cells will divide at different volumes however.
lengtha = 0.1 

# specify target volumes (different for each type )
targetVola = 2*initialVola
targetVolb = 2*initialVolb
targetVolc = 2*initialVolc
targetVold = 2*initialVold

max_cells = 6000 # based on 5000 max
saveEvery = 10
cell_colors = {1:[1.0, 0.0, 0.0],\
			   0:[0.0, 0.0, 1.0]}

def setup(sim):

	# Set biophysics, signalling, and regulation models. Add dolfin solver if used.
	biophys = CLBacterium(sim, 
						  max_substeps=8, 
						  max_cells=max_cells, 
						  max_contacts=32,
						  max_sqs=100**2,
						  jitter_z=False,
						  reg_param=0.04,
						  gamma=500,
						  periodic=False,
						  grid_spacing=10.0)

	# add mechanical planes
	planeWeight = 1.0
	biophys.addPlane((0,0,0),   (0,1,0), planeWeight) 		# base of box
					 
	regul = ModuleRegulator(sim, __file__)	# use this file for reg too

	# compile a list of solver parameters (using scaled values)
	solverParams = None

	# add biophysics, regulation, [solver], objects to simulator
	sim.init(biophys, regul, None, None, solverParams)

	# initialise 2 cells with same lengths, radii at first
	# this will be the same for each combination
	sim.addCell(cellType=0, len=lengtha, rad=radius, pos=(-3,radius,0), dir=(1,0,0))
	sim.addCell(cellType=1, len=lengtha, rad=radius, pos=(+3,radius,0), dir=(1,0,0))
	
	# Add some objects to draw the models
	mainRenderer = Renderers.GLBacteriumRenderer(sim)
	sim.addRenderer(mainRenderer)

	# How often should we output data?
	sim.renderEveryNSteps = 1
	sim.savePickle = True
	sim.pickleSteps = saveEvery
	print "Ready."

def init(cell):
	if cell.cellType==0:
		cell.targetVol = targetVola + random.uniform(0.0,0.09*targetVola)
		cell.growthRate = 1

	if cell.cellType==1:
		cell.targetVol = targetVolc + random.uniform(0.0,0.09*targetVolc)
		cell.growthRate = 1

def numSignals():
    return 0

def numSpecies():
    return 0

def update(cells):
    for (id, cell) in cells.iteritems():
    
    	# why are we rewriting the color every update call?
        cell.color = cell_colors[cell.cellType]
        
        # division checks
        if cell.volume > cell.targetVol:
            cell.asymm = [1,1]
            cell.divideFlag = True
        

def divide(parent, d1, d2):

    if parent.cellType==0:
		d1.targetVol = targetVola + random.uniform(0.0,0.09*targetVola)
		d2.targetVol = targetVola + random.uniform(0.0,0.09*targetVola)
    	
    if parent.cellType==1:
		d1.targetVol = targetVolc + random.uniform(0.0,0.09*targetVolc)
		d2.targetVol = targetVolc + random.uniform(0.0,0.09*targetVolc)
    
def kill(cell):
	cell.growthRate = 0.0   	# dead cells can't grow any more
	cell.divideFlag = False		# dead cells can't divide