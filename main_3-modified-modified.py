from __future__ import print_function
n = 7# input('n: ')

# 1. Take input and define objective & constraints
def take_input():
	global s,r,c,m,fi
	million = 10**6
	thousand = 10**3
	s = 550#input('s: ')
	r = 50 #input('r: ')
	c = 0.6#input('c: ')
	m = 0.5#input('m: ')
	fi = 4*million #input('fi: ')

	global T,M,C,R
	T = 1#input('T: ')
	M = 20*million# input('M: ')
	C = 10*million# input('C: ')
	R = 90*thousand# input('R: ')

	global d, gbar, y 
	d = 0.15#input('d: ')
	gbar = 0.65#input('gbar: ')
	y = 0.9#input('y: ')
	
take_input()

import random
import numpy


for i in range(1,n+1):
	iteration = 0
	objective_function_value_all = []
	variable_list_all            = []
	
	while iteration<3:
		iteration+=1
		#print(iteration)
		SEED = 1
		objective_function_value = -1
		while objective_function_value<0:
			
			import platypus# import NSGAII, Problem, Real
			import importlib
			
			numpy.random.seed(1)
			random.seed(1)
			importlib.reload(platypus)
			numpy.random.seed(1)
			random.seed(1)
			
			def belegundu(l):	
				Qm_i, Qc_i, Qr_i = l
				
				if iteration==1:
					v_i =( (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qm_i/M)  )/ ( (1+d)**i)
				elif iteration==2:
					v_i =( (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qc_i/C)  )/ ( (1+d)**i)
				elif iteration==3:
					v_i =( (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qr_i/R)  )/ ( (1+d)**i)
				
				#v_i = (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qm_i/M) / ( (1+d)**i)
				
				c1 = Qr_i - gbar*y*Qc_i
				
				return [v_i], [c1]

			# 2. Running Gen-Algo
			problem = platypus.Problem(3, 1, 1)  # n_variables, n_objectiveFuncs, n_constraints
			problem.types[:] = [platypus.Real(0, M), platypus.Real(0, C), platypus.Real(0, R)]
			problem.constraints[:] = "==0"
			problem.function = belegundu
			
			algorithm = platypus.NSGAII(problem)
			algorithm.run(1000*100)

			
			# 3. Outputing best value
			temp = []
			for solution in algorithm.result:
				temp.append(solution.objectives[0])
			index = numpy.argmax(temp)
			objective_function_value = algorithm.result[index].objectives[0]
			#print;print('  ',objective_function_value)
			variable_list            = algorithm.result[index].variables
			if objective_function_value>0:
				objective_function_value_all.append(objective_function_value) 
				variable_list_all.append(variable_list)
				
			SEED +=1
			
	objective_function_value = min(objective_function_value_all) 		
	index_                   = objective_function_value_all.index(objective_function_value)
	variables                = variable_list_all[index_]
	
	print 
	print("Best Value:",objective_function_value)
	print("Best Value parameters:",variables)
	Fi = (d*objective_function_value)/C
	print('Step',str(i)+":")
	print('    Fi    = ',Fi)
	print('    gm(i) = ',(m+c+(fi/C)+Fi)/((s-r)*y)  ); print("=================")


