"""
Docstring for 10.Part 1.pt1

Solve using a system of equations
Find the subspace of possible solutions, 
then iterate to find the lowest one
"""

from sympy import *
import numpy as np


def valid(vec):
    """
    Returns true if a vector is all non-negative integers

    :param vec: The vector to check
    """

    for x in vec:
        if abs(x - round(x)) > 1e-7 or x < -1e-5:
            return False
    return True


with open("10/Part 1/in.txt", "r") as f:
    rtn = 0

    for line in f.readlines():
        tokens = line.strip().split()
        buttons = tokens[1:-1]
        joltage = tokens[-1]

        # Converting lights
        y = [int(x) for x in joltage.strip('{').strip('}').split(',')]
        m = len(y)
        n = len(buttons)
        buttons = [[int(x) for x in buttons[j].strip('(').strip(')').split(',')] for j in range(n)]
        # Construct an m x n matrix
        matrix = [[0 for _ in range(n + 1)] for __ in range(m)]

        for i in range(n):
            for j in buttons[i]:
                matrix[j][i] = 1
                matrix[j][-1] = y[j]
        
        rref = Matrix(matrix).rref()

        # Constructing span of solution set
        b = []
        for i in range(n):
            if i not in rref[1]:
                b.append(0)
            else:
                b.append(rref[0][rref[1].index(i), -1])
        b = np.array(b, dtype=np.float64)  # The constant term in the solution

        vectors = []
        for i in range(n):
            if i not in rref[1]:
                vec = np.zeros(n)
                for j in range(len(rref[1])):
                    vec[rref[1][j]] = -rref[0][j, i]
                vec[i] = 1
                vectors.append(np.array(vec, dtype=np.float64))

        if len(vectors) == 0:
            # Simple case where there is one unique solution
            rtn += sum(b)
        else:
            # Multiple degrees of freedom (1-3)
            # We just do 3 explicit cases

            RANGE = range(max(y)) # Search space
            lowest = np.inf
            if len(vectors) == 1:
                for x in RANGE:
                    temp = b + x * vectors[0]
                    if valid(temp):
                        lowest = min(lowest, int(sum(temp)))
                if lowest == np.inf:
                    print("1!!!!!")
            elif len(vectors) == 2:
                for x in RANGE:
                    for y in RANGE:
                        temp = b + x * vectors[0] + y * vectors[1]
                        if valid(temp):
                            lowest = min(lowest, int(sum(temp)))
                if lowest == np.inf:
                    print("2!!!!!")
            elif len(vectors) == 3:
                for x in RANGE:
                    for y in RANGE:
                        for z in RANGE:
                            temp = b + x * vectors[0] + y * vectors[1] + z * vectors[2]
                            if valid(temp):
                                lowest = min(lowest, int(sum(temp)))
                if lowest == np.inf:
                    print("3!!!!!")
            rtn += lowest
            
    print(rtn)
