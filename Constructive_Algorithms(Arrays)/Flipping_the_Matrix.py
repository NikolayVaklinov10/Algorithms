import math
import os
import random
import re
import sys


def flippingMatrix(matrix):
    s = 0
    k = len(matrix[0])
    for i in range(int(k/2)):
        for j in range(int(k/2)):
            s += max(matrix[i][j], matrix[i][k-j-1], matrix[k-i-1][j], matrix[k-i-1][k-j-1])
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
