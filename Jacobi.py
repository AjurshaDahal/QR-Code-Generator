# x(k+1) - inv(D)[(-L-U)x(k)+b]

from numpy import array,diag,diagflat,dot
import numpy as np
from numpy.linalg import inv

#for number of iteration
N= 20
A = array([[2,1,1],[1,3,-1],[-1,1,2]])
b = array([6,0,3])

guess = array([0,0,0])
# upper triangular and lower triangular
U = np.triu(A,1)
L = np.tril(A,-1)
# diagonal matrix
D = diagflat(diag(A))
#inverse of diagonal matrix
inv_of_D = inv(D)

sub_L_U = -L-U

# x(k+1) - inv(D)[(-L-U)x(k)+b]

for i in range (N):
    mult_LU = dot(sub_L_U, guess) + b
    guess = dot(inv_of_D,mult_LU) 
    print (i+1, np.round(guess,5))




