import numpy as np

#initialize vectors and matrix
x = np.array([[0],[0],[0]])
y = np.array([[0],[0],[0]])
A = np.zeros((3,3))

#input x
x[0] = input("x0 = ")
x[1] = input("x1 = ")
x[2] = input("x2 = ")


#input y
y[0] = input("y0 = ")
y[1] = input("y1 = ")
y[2] = input("y2 = ")


#construct the NxM vandermonde matrix
for n in range(3):
	for m in range(3):
		A[n,m] = (int(x[n])) ** m

#construct A inverse
A_inverse = np.linalg.inv(A)

# solve, Ax = b => x = Ainverse b
# a0*x^0 + a1*x^1 + a2*x^2 = f(x)

solution = A_inverse.dot(y)
 
print("f(x) = " + str(solution[0]) + " + " + str(solution[1]) + "x + " + str(solution[2]) + "x^2")