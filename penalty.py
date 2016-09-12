import math
import numpy as np
from scipy.optimize import linprog

#f(x) = x^2 + y^2 -> min
#g(x) = 2x + y + 4 <= 0


fib = (1+math.sqrt(5))/2

def fi(x,r):
	res = 2*x[0]+x[1]+4 
	if res < 0:
		return x[0]**2+x[1]**2
	return x[0]**2+x[1]**2+r*res**2

def gradfi(x,r):
	res = 2*x[0]+x[1]+4 
	if res < 0:
		return np.array([2*x[0],2*x[1]])
	return np.array([2*x[0]+4*r*res, 2*x[1]+2*r*res])

def H(x):
	res = 2*x[0]+x[1]+4 
	if res < 0:
		return 0
	return res**2	


def golden_search(a,b,f,xk,r,grad,eps):
	global fi
	while abs(b-a) > eps:
		x1 = b - (b-a)/fib
		x2 = a + (b-a)/fib
		
		y1 = f(xk-x1*grad,r)
		y2 = f(xk-x2*grad,r)
		

		if y1 >= y2:
			a = x1
			x1 = x2
			x2 = a + (b-a)/fib
		else:
			b = x2
			x2 = x1
			x1 =b - (b-a)/fib
	return (a+b)/2

xk = [1, 1]
rk = 1
eps = 0.01
eps1 = 0.00001

a = -10
b = 10
gradk = gradfi(xk,rk)

while H(xk) > eps:
	while np.linalg.norm(gradk) > eps1:
		alpha = golden_search(a,b, fi, xk,rk, gradk, eps1)
		xk = xk - alpha*gradk
		gradk = gradfi(xk,rk)
	rk = 10*rk
	gradk = gradfi(xk,rk)




print(alpha)
print(xk)