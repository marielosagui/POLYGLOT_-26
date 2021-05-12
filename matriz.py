from array import array

#Fun para llenae una matriz nxn
def matrixcero(Matrix, n):
    for i in range(n):
        Matrix.insert(i,array('f', (0.0 for i in range(n))))

#fun llenar arreglo n con ceros
def arraycero(Array, n):
    for i in range(n):
        Array.append(0.0)

#fun para copiar elementos de una matriz A a otra B
def copyMatrix(A, B):
    matrixcero(B, len(A))
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            B[i][j] = A[i][j]

#fun producto de una Matrix M por un arreglo
def productoMxV(M, V, R):
    n = len(M)
    for i in range(n):
        m = len(V)
        cell = 0.0
        for j in range(m):
            cell += M[i][j] * V[j]
        R[i] += cell

#fun producto de un numero real por cada uno de los elementos de una matriz
def productoRMatrix(real, M, R):
    n = len(M)
    m = len(M[0])
    matrixcero(R, n)
    for i in range(n):
        for j in range(m):
            R[i][j] = real * M[i][j]

#fun calcula el menor de una matriz 
def menorm(M, i, j):
    M.pop(i)
    n = len(M)
    for k in range(0,n):
        M[k].pop(j)

#funcion calcula el determinante de una matriz
def determinantem(M):
    if len(M) == 1:
        return M[0][0]
    else:
        det = 0.0
        for i in range(0,len(M[0])):
            menor = []
            copyMatrix(M, menor)
            menorm(menor, 0, i)
            det = det + ((-1)**i)*M[0][i]*determinantem(menor)
        return det

#Calcula la matriz de cofactores
def mcofactores(M, Cof):
    n = len(M)
    m = len(M[0])
    matrixcero(Cof, n)
    for i in range(n):
        for j in range(m):
            menor = []
            copyMatrix(M, menor)
            menorm(menor,i,j)
            #calcula el cofactor y se alamcena en la matriz de cofactores en la celda i,j
            Cof[i][j] = ((-1)**(i+j))*determinantem(menor)

#fun calcula la transpuesta de una matriz M, y almacena el resultado en la matriz T
def transpuesta(M, T):
    n = len(M)
    m = len(M[0])
    matrixcero(T, n)
    for i in range(n):
        for j in range(m):
            T[j][i] = M[i][j]

#inversa de una matriz utilizando el metodo de la adjunta
def Minversa(M, Minv):
    det = determinantem(M)
    if det == 0:
        print("exit")
        exit()
    else:
        cofactores = []
        adjunta = []
        mcofactores(M,cofactores)
        transpuesta(cofactores,adjunta)
        productoRMatrix(1/det, adjunta, Minv)