from numpy import array, diag, diagflat, dot
import numpy as np
from numpy.linalg import inv

# Input number of equations (size of the matrix)
n = int(input("Enter the number of variables (n x n matrix): "))

# Input the matrix A
print("Enter the coefficients matrix A (row by row):")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    if len(row) != n:
        print(f"Error: Row {i + 1} must contain {n} elements.")
        exit()
    A.append(row)
A = array(A)

# Input the vector b
print("Enter the constant vector b:")
b = []
for i in range(n):
    b.append(float(input(f"b[{i + 1}]: ")))
b = array(b)

# Input the initial guess vector
print("Enter the initial guess vector (default is 0 for all elements):")
guess = []
for i in range(n):
    inp = input(f"Initial guess for x[{i + 1}] (press Enter for 0): ")
    guess.append(float(inp.strip()) if inp else 0)
guess = array(guess)

# Input the number of iterations
N = int(input("Enter the number of iterations: "))

# Prepare for the Jacobi method
U = np.triu(A, 1)  # Upper triangular matrix
L = np.tril(A, -1)  # Lower triangular matrix
D = diagflat(diag(A))  # Diagonal matrix
inv_of_D = inv(D)  # Inverse of diagonal matrix
sub_L_U = -L - U  # (-L-U)

# Jacobi iteration
for i in range(N):
    mult_LU = dot(sub_L_U, guess) + b
    guess = dot(inv_of_D, mult_LU)
    print(f"Iteration {i + 1}: {np.round(guess, 5)}")
