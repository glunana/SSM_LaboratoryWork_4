matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1]
]

def reflexivity(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i][i] != 1:
            return False
    return True

print("Відношення є рефлексивне: ", reflexivity(matrix))

def antireflexivity(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i][i] != 0:
            return False
    return True

print("Відношення є антирефлексивне: ", antireflexivity(matrix))

def symmetry(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

print("Відношення є симетричне: ", symmetry(matrix))

def asymmetry(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] == matrix[j][i] == 1:
                return False
    return True

print("Відношення є асиметричне: ", asymmetry(matrix))

def antisymmetry(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == matrix[j][i] == 1:
                return False
    return True

print("Відношення є антисиметричне: ", antisymmetry(matrix))

def transitivity(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == 0:
                        return False
    return True

print("Відношення є транзитивне: ", transitivity(matrix))

def antitransitivity(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == 1:
                        return False
    return True

print("Відношення є антитранзитивне: ", antitransitivity(matrix))

def equivalence(matrix):
    if symmetry(matrix) and reflexivity(matrix) and transitivity(matrix):
        return True
    else:
        return False

print("Відношення є еквівалентним: ", equivalence(matrix))

def partialOrder(matrix):
    if reflexivity(matrix) and antisymmetry(matrix) and transitivity(matrix):
        return True
    else:
        return False

print("Відношення є частковим порядком: ", partialOrder(matrix))

def strictOrder(matrix):
    if antireflexivity(matrix) and antisymmetry(matrix) and transitivity(matrix):
        return True
    else:
        return False

print("Відношення є строгим порядком: ", strictOrder(matrix))


def reflexivMatrix (matrix):

    matrixR = [row[:] for row in matrix]
    n = len(matrixR)

    for i in range(n):
        matrixR[i][i] = 1
    return matrixR

print("Рефлексивне замикання: ")
matrixR = reflexivMatrix(matrix)

for row in matrixR:
    print(row)

def symmetryMatrix(matrix):

    matrixS = [row[:] for row in matrix]
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrixS[i][j] == 1:
                matrixS[j][i] = 1
    return matrixS

print("Симетричне замикання: ")
matrixS = symmetryMatrix(matrix)

for row in matrixS:
    print(row)

def transitivityMatrix(matrix):
    matrixT = [row[:] for row in matrix]
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrixT[i][j] == 1:
                for k in range(n):
                    if matrixT[j][k] == 1 and matrixT[i][k] == 0:
                        matrixT[i][k] = 1
    return matrixT

print("Транзитивне замикання: ")
matrixT = transitivityMatrix(matrix)

for row in matrixT:
    print(row)

def squareMatrix(matrix):
    n = len(matrix)
    matrixSq = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrixSq[i][j] = matrixSq[i][j] or (matrix[i][k] and matrix[k][j])

    return matrixSq

print("2 степінь: ")
matrixSq = squareMatrix(matrix)

for row in matrixSq:
    print(row)

def cubedMatrix(matrix):
    matrixSq = squareMatrix(matrix)

    matrixCu = squareMatrix(matrixSq)
    return matrixCu

print("3 степінь: ")
matrixCu = cubedMatrix(matrix)

for row in matrixCu:
    print(row)











