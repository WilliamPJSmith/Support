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

# specify target volumes (different for each type )
targetVola = 2*initialVola
targetVolb = 2*initialVolb
targetVolc = 2*initialVolc
targetVold = 2*initialVold

max_cells = 11000 # based on 7500 max
num_initial_cells = 75
saveEvery = 10
cell_colors = {0:[1.0, 0.0, 0.0],\
			   1:[0.0, 0.0, 1.0]}
			   
# extra info for nutrients:
meshParam = 10.0
Num_x = 30; Num_y = 15
Len_x = Num_x*meshParam
Len_y = Num_y*meshParam 

# random seed for replicatability
#Seed = 1
#numpy.random.seed(Seed)

def setup(sim):

	# Set biophysics, signalling, and regulation models. Add dolfin solver if used.
	biophys = CLBacterium(sim, 
						  max_substeps=8, 
						  max_cells=max_cells, 
						  max_contacts=32,
						  max_sqs=Num_x*Num_y,
						  jitter_z=False,
						  reg_param=0.04,
						  gamma=500,
						  periodic=False,
						  grid_spacing=meshParam,
						  L_x = Len_x, 
						  L_y = Len_y)

	# add mechanical planes
	planeWeight = 1.0
	biophys.addPlane((0,0,0), (0,1,0), planeWeight) 		    # base of box
	
	# what happens if we add some sides?
	biophys.addPlane((0,0,0),   (+1,0,0), planeWeight) 			# left side
	biophys.addPlane((Len_x,0,0), (-1,0,0), planeWeight) 		# right side
					 
	regul = ModuleRegulator(sim, __file__)	# use this file for reg too

	# compile a list of solver parameters (using scaled values)
	""" CASE 1 - HIGH NUTRIENTS """

	solverParams = dict(h = 0.5*meshParam, 
					origin = [0.0,0.0,0.0],
					N_x = 2*Num_x,
					L_x = Len_x,
					u0 = 1.0,
					K = 0.0033,
					mu_eff = 0.001,
					pickleSteps = 10,
					rel_tol = 1e-6,
					mesh_type = 'crossed',
					delta = 40.0)
	
	# add biophysics, regulation, [solver], objects to simulator
	sim.init(biophys, regul, None, None, solverParams)

	# randomly initialise a line of cells along the bottom
	RandomSeedOnLine(sim, Len_x, num_initial_cells, initialVola, initialVola, radius)
	
	# Add some objects to draw the models
	mainRenderer = Renderers.GLBacteriumRenderer(sim)
	sim.addRenderer(mainRenderer)


	# How often should we output data?
	sim.renderEveryNSteps = 1
	#sim.savePickle = True
	sim.pickleSteps = saveEvery
	print "Ready."


def init(cell):
	if cell.cellType==0:
		cell.targetVol = targetVola + random.uniform(0.0,0.09*targetVola)
		cell.growthRate = 1

	if cell.cellType==1:
		cell.targetVol = targetVold + random.uniform(0.0,0.09*targetVold)
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
		d1.targetVol = targetVold + random.uniform(0.0,0.09*targetVold)
		d2.targetVol = targetVold + random.uniform(0.0,0.09*targetVold)
    
    
def kill(cell):
	cell.growthRate = 0.0   	# dead cells can't grow any more
	cell.divideFlag = False		# dead cells can't divide


def RandomSeedOnLine(sim, L_x, N, vola, volb, R):

	# begin by randomly assigning cells one of 2 types
	Nb = int(numpy.floor(N*0.5));         		# half the cells will be type 'b'
	shuffledInds = range(0,N)					# get inds 0 to N-1
	numpy.random.shuffle(shuffledInds)			# shuffle the inds
	Types = numpy.zeros(N);   					# all cells are type 'a' by default
	Types[shuffledInds[0:Nb]] = 1;    			# make the first Nb cells in shuffledInds 'b'

	# inital volumes and lengths
	V0s = vola*numpy.ones(N)
	V0s[shuffledInds[0:Nb]] = volb
	Vols = V0s*(numpy.random.random(N) + 1)      # volumes are drawn randomly from U(V0, 2*V0); V0 depends on type	
	Lens = Vols/(math.pi*R**2) - 4*R/3.0		# all cells have same radius; work lengths out from vols irrespective of type

	# having assigned cell types and volumes, randomly assign positions
	Spans = 0.5*(Lens + 2*R) 					# half the footprint each cell makes on the x axis

	# create a table of position data to sort

	#Data = numpy.zeros((N+2.3), dtype=[('x',float), ('y',float), ('z',int)])
	Data = numpy.zeros((N+2,3))
	Data[1:N+1,1] = Spans
	Data[1:N+1,2] = 1
	Data[-1,0] = L_x
	
	# loop where we check for overlapping cells and remove them
	num_flags = N; iter = 0
	while num_flags > 0:
	
		# any cell with a flag gets a new position drawn
		Data[Data[:,2]>0,0] = L_x*numpy.random.random(num_flags)							
	
		# sort cells by x coordinate
		temp = Data.view(numpy.ndarray)
		Data = temp[numpy.lexsort((temp[:, 0], ))]
   
		# flags are reset, then recomputed
		Data[:,2] = 0
		Data[numpy.diff(Data[:,0])-Data[0:N+1,1]-Data[1:N+2,1] < 0,2] = 1
	
		# if left wall has been flagged, pass flag to 1st cell on left
		if Data[0,2] == 1:
			Data[0,2] = 0; Data[1,2] = 1
	
		# update the flag and iter counts
		num_flags = numpy.sum(Data[:,2]); iter+=1
		
	print 'Random seed on line complete after %i iterations' % iter
	Pos = numpy.zeros((N,3))
	Pos[:,0] = Data[1:N+1,0]
	Pos[:,1] = R
		
	# add cells to the population
	for i in range(0,N):
		sim.addCell(cellType=Types[i], len=Lens[i], rad=R, pos=tuple(Pos[i,:]), dir=tuple([1,0,0]))