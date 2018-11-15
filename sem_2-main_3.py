n = 1# input('n: ')

for i in range(n):

	from scipy import optimize

	def take_input():
			global s,r,c,m,fi
			million   = float(10**6)
			thousand  = float(10**4)
			s         = 550      #input('s: ')
			r         = 50       #input('r: ')
			c         = 0.6      #input('c: ')
			m         = 0.5      #input('m: ')
			fi        = 4*million#input('fi: ')

			global T,M,C,R
			T         = 1         #input('T: ')
			M         = 20*million#input('M: ')
			C         = 10*million#input('C: ')
			R         = 90*thousand#input('R: ')

			global d, gbar, y 
			d         = 0.15      #input('d: ')
			gbar      = 0.65      #input('gbar: ')
			y         = 0.9       #input('y: ')

	def func(l):

			Qm_i, Qc_i, Qr_i = l

			p_i       = (s-r)*Qr_i - m*Qm_i - c*Qc_i - fi*T
			f_i       = p_i/( (1+d)**i) 
			
			return -f_i

	take_input()
	bnds=((0,M),(0,C),(0,R))

	cons=({'type':'eq','fun':lambda x: x[2] - gbar*y*x[1]})
	x0=[1,1,1]
	res= optimize.minimize(func,x0,method='SLSQP',bounds=bnds,constraints=cons)
	
	print ''
	objective_function_value = res['fun']
	print "Best Value:",-1*objective_function_value
	print "Best Value parameters:",list(res['x'])
	Fi = (d*objective_function_value)/C
	print 'Step',str(i)+":"
	print '    Fi    = ',Fi
	print '    gm(i) = ',(c+(fi/C)+Fi)/((s-r)*y); print 

raw_input()


