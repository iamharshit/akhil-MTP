
n = 1# input('n: ')

for i in range(n):
        from platypus import NSGAII, Problem, Real
        import sys
        import numpy as np

        # 1. Take input and define objective & constraints
        def take_input():

                global s,r,c,m,fi
                million = 10**6
                thousand = 10**4
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
                
        def belegundu(l):
            Qm_i, Qc_i, Qr_i = l

            p_i = (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*T
            v_i = p_i/( (1+d)**i) 
            
            c1 = Qr_i - gbar*y*Qc_i
            
            return [v_i], [c1]

        take_input()

        # 2. Running Gen-Algo
        problem = Problem(3, 1, 1)  # n_variables, n_objectiveFuncs, n_constraints
        problem.types[:] = [Real(0, M), Real(0, C), Real(0, R)]
        problem.constraints[:] = "==0"
        problem.function = belegundu

        algorithm = NSGAII(problem)
        algorithm.run(100*100*10)


        # 3. Outputing best value
        '''
        print 'Solution:'
        for solution in algorithm.result:
            print(solution.objectives), solution.variables
        '''
        index = np.argmax(algorithm.result)
        objective_function_value = algorithm.result[index].objectives[0]
        print 
        print "Best Value:",objective_function_value
        print "Best Value parameters:",algorithm.result[index].variables
        Fi = (d*objective_function_value)/C
        print 'Step',str(i)+":"
        print '    Fi    = ',Fi
        print '    gm(i) = ',(c+(fi/C)+Fi)/((s-r)*y); print 

raw_input()
