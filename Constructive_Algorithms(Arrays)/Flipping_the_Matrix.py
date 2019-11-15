def flippingMatrix(matrix):
    s = 0
    k = len(matrix[0])
    for i in range(int(k/2)):
        for j in range(int(k/2)):
            s += max(matrix[i][j], matrix[i][k-j-1], matrix[k-i-1][j], matrix[k-i-1][k-j-1])
    return s

