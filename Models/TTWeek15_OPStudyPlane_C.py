import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy
import math

# calculate radii
radiusA = 0.76
radiusB = 0.63
radiusC = 0.56
radiusD = 0.48
radius = radiusC
type = 2

# specify target volume (same for each type, limited by smallest volume allowing spheres to have L>0)
initialVol = 1.85
targetVol = 2*initialVol

# specify initial lengths
length = initialVol/(math.pi*radius**2) - 4*radius/3.0

max_cells = 10000
saveEvery = 10
cell_colors = {0:[1.0, 0.0, 0.0],1:[0.5, 0.0, 0.0],2:[0.0, 0.0, 0.5],3:[0.0, 0.0, 1.0]}
			   

def setup(sim):

	# Set biophysics, signalling, and regulation models. Add dolfin solver if used.
	biophys = CLBacterium(sim, 
						  max_substeps=8, 
						  max_cells=max_cells, 
						  max_contacts=32,
						  max_sqs=100**2,
						  jitter_z=True,
						  reg_param=0.04,
						  gamma=500,
						  periodic=False,
						  grid_spacing=10.0)

	# add mechanical planes
	planeWeight = 1.0
	biophys.addPlane((0,0,0), (0,1,0), planeWeight) 		# base of box

	regul = ModuleRegulator(sim, __file__)	# use this file for reg too

	# compile a list of solver parameters (using scaled values)
	solverParams = None

	# add biophysics, regulation, [solver], objects to simulator
	sim.init(biophys, regul, None, None, solverParams)

	# initialise 2 cells with different lengths, radii
	sim.addCell(cellType=type, len=length, rad=radius, pos=(0,0,radius), dir=(1,0,0))
	
	# Add some objects to draw the models
	mainRenderer = Renderers.GLBacteriumRenderer(sim)
	sim.addRenderer(mainRenderer)

	# How often should we output data?
	sim.renderEveryNSteps = 1
	sim.savePickle = True
	sim.pickleSteps = saveEvery
	print "Ready."

def init(cell):
    cell.targetVol = targetVol + random.uniform(0.0,0.09*targetVol)
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
    d1.targetVol = targetVol + random.uniform(0.0,0.09*targetVol)
    d2.targetVol = targetVol + random.uniform(0.0,0.09*targetVol)
    
def kill(cell):
	cell.growthRate = 0.0   	# dead cells can't grow any more
	cell.divideFlag = False		# dead cells can't divide
	
