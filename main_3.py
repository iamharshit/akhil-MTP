
n = 7# input('n: ')

for i in range(n):
        from platypus import NSGAII, Problem, Real
        import sys
        import numpy as np

        # 1. Take input and define objective & constraints
        def take_input():

                global s,r,c,m,fi
                million = 10**6
                thousand = 10**3
                s = 550#input('s: ')
                r = 50#input('r: ')
                c = 0.6#input('c: ')
                m = 0.5#input('m: ')
                fi = 4*million#input('fi: ')

                global T,M,C,R
                T = 1#input('T: ')
                M = 20*million#input('M: ')
                C = 10*million#input('C: ')
                R = 90*thousand#input('R: ')

                global d, gbar, y 
                d = 0.15#input('d: ')
                gbar = 0.0065#input('gbar: ')
                y = 0.9#input('y: ')
                
        def belegundu(l):
            Qm_i, Qc_i, Qr_i = l

            p_mi = (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qm_i/M)
            v_mi = 1*p_mi/( (1+d)**i) 
			
            p_ci = (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qc_i/C)
            v_ci = 1*p_ci/( (1+d)**i) 
			
            p_ri = (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*(Qr_i/R)
            v_ri = 1*p_ri/( (1+d)**i) 
            
            c1 = Qr_i - gbar*y*Qc_i
            
            return [v_mi, v_ci, v_ri], [c1]
			
        def argmax_custom(arr):
                        maxi = -float('inf')
                        ans  = None
                        for index, solution in enumerate(arr):
                               if maxi < sum(solution.objectives):
                                        maxi = sum(solution.objectives)
                                        ans = index
                        return ans
			
        take_input()

        # 2. Running Gen-Algo
        problem = Problem(3, 3, 1)  # n_variables, n_objectiveFuncs, n_constraints
        problem.types[:] = [Real(0, M), Real(0, C), Real(0, R)]
        problem.constraints[:] = "==0"
        problem.function = belegundu

        algorithm = NSGAII(problem)
        algorithm.run(10000)


        # 3. Outputing best value
        '''
        print 'Solution:'
        for solution in algorithm.result:
            print solution.objectives, solution.variables
        '''
        index = argmax_custom(algorithm.result)
        objective_function_value = min(algorithm.result[index].objectives)
        print 
        print "Best Value:",objective_function_value
        print "Best Value parameters:",algorithm.result[index].variables
        Fi = (d*objective_function_value)/C
        print 'Step',str(i)+":"
        print '    Fi    = ',Fi
        print '    gm(i) = ',(c+(fi/C)+Fi)/((s-r)*y); print 

raw_input()
