import numpy as np 
import matplotlib.pyplot as plt 

q = np.array([[0.7654, 1-0.7654],
			 [0.1223, 1-0.1223],
			 [0.9645, 1-0.9645],
			 [0.6319, 1-0.6319],
			 [0.3614, 1-0.3614]]
			 )

p = np.array([[1,0],
			  [0,1],
			  [1,0],
			  [1,0],
			  [0,1]]
			  )

def cross_entropy(p,q):
	n = len(p)
	return - np.sum(p*np.log(q))/n

def quadratic(p,q):
	n = len(p)
	return np.sum([(p[i]-q[i])**2 for i in range(len(p))])/n

print("cross entropy loss: ",cross_entropy(p,q))
print("quadratic loss: ",quadratic(p,q))