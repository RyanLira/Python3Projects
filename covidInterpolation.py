#Ryan Lira May 28, 2022
# This program takes in a set of data over the course of a set number of days
# it forms a NxN vandermonde matrix from the number of days 
# and a collumn vector made up of the input corsponding to those days
# then it uses those elements to solve the matrix equation Ax = y
# and returns x
# this x vector makes up the coefficients in a vandermonde polynomial
# which can then be used to predict future events

import numpy as np

##INPUT##################################################
numberOfDays = int(input("how many days: "))
deaths = np.zeros([numberOfDays])
for n in range(numberOfDays):
	deaths[n] = input(f'deaths on day {n} : ')


##PROCESS###############################################
# initialize vandermonde matrix
vandermond_matrix = np.zeros([numberOfDays, numberOfDays])

# populate the vandermone matrix
for i in range(numberOfDays): 
	for j in range(numberOfDays):
		vandermond_matrix[i,j] = int(pow(i, j))

#solve
x = np.linalg.solve(vandermond_matrix, deaths)


##OUTPUT###############################################
print(x)