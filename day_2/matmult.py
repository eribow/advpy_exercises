#!/usr/bin/python
# Program to multiply two matrices using nested loops
import random

N = 250

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

len_X=len(X)
len_Y=len(Y)
len_Y_0=len(Y[0])

# iterate through rows of X
for i in range(len_X):
    # iterate through columns of Y
    for j in range(len_Y_0):
        # iterate through rows of Y
        for k in range(len_Y):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
