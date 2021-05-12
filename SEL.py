from banco import *
from class import *
from matriz import *
from array import array

#funcion que  muestra la matriz
def muestra_matriz(K):
    n = len(K[0])
    m = len(K)
    for i in range(n):
        print("[\t", end="")
        for j in range(m):
            print(round(K[i][j],4),end="\t")
        print("]")
    print("")

#fun para mostrar las Ks locales
def muestraKs(Ks):
    n = len(Ks)
    for i in range(n):
        print("K del elemento ",i+1,":")
        muestra_matriz(Ks[i])
        print("-------------------------------")
    print("")

#fun para mostrar las bs locales
def muestraBs(bs):
    n = len(bs)
    for i in range(n):
        print("b del elemento",i+1)
        muestraArray(bs[i])
        print("-------------------------------")
    print("")

#fun muestra los valores de un arreglo 
def muestraArray(b):
    print("",end="[\t")
    n = len(b)
    for i in range(n):
        print(round(b[i],5),end="\t")
    print("]", end ="\n")

#fun que recibe la malla y devuelve la matriz K local
def crea_localK(m):
    K = []
    row1 = array('f')
    row2 = array('f')
    k = m.getParameter(PARAMETERS['THERMAL_CONDUCTIVITY'])
    l = m.getParameter(PARAMETERS['ELEMENT_LENGHT'])
    #valores a las celdas de la matriz = (k/L)[{1,-1}{-1,1}] 
    row1.append(k/l); row1.append(-k/l)
    row2.append(-k/l); row2.append(k/l)
    K.append(row1); K.append(row2)
    return K #retornamos la matriz K

#fun recibe la malla y devuelve el vector b local
def crea_localB(m):
    b = array('f') #
    Q = m.getParameter(PARAMETERS['HEAT_SOURCE'])
    l = m.getParameter(PARAMETERS['ELEMENT_LENGHT'])
    #valores al arreglo = [Q*(l/2),Q*(l/2)]
    b.append(Q*l/2); b.append(Q*l/2)
    return b

#fun crea los sitemas locales K y b
def crearSistemasLocales(m, localKs, localbs):
    for i in range(m.getSize(SIZES['elements'])):
        localKs.append(crea_localK(m))
        localbs.append(crea_localB(m))


#fun realiza el ensamblaje de la matriz K global
def ensamblajeK(e, localK, K):
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1
    K[index1][index1] += localK[0][0]
    K[index1][index2] += localK[0][1]
    K[index2][index1] += localK[1][0]
    K[index2][index2] += localK[1][1]


#fun hace el ensamblaje del arreglo b global, recibe el elemento actual, el arreglo b local
def ensamblajeB(e, localb, b):
    index1 = e.getNode1()-1
    index2 = e.getNode2()-1
    b[index1] += localb[0]
    b[index2] += localb[1]


#ensamblaje de los sistemas locales K y B 
def ensamblaje(m, localKs, localbs, K, b):
    for i in range(m.getSize(SIZES['elements'])):
        e = m.getElement(i)
        ensamblajeK(e, localKs[i], K)
        ensamblajeB(e, localbs[i], b)

#condicion de Neumann en el arreglo b global
def Neumann(m, b):
    for i in range(m.getSize(SIZES['neumann'])):
        c = m.getCondition(i, SIZES['neumann'])
        b[c.getNode1()-1] += c.getValue()

#condicion de dirichlet al sistema de ecuaciones matriciales.
# Recibe la malla, la matriz K global y el arreglo b global
def Dirichlet(m, K, b):
    for i in range(m.getSize(SIZES['dirichlet'])):
        c = m.getCondition(i, SIZES['dirichlet'])
        index = c.getNode1() - 1
        del K[index]
        b.pop(index)
        s = len(K)
        for i in range(s):
            cell = K[i][index]
            K[i].pop(index)
            b[i] += -1*c.getValue()*cell

#fun que  calcula la sol del sistema de ecuaciones y lo almacena en el arreglo T
def calculo(K, b, T):
    #Se crea la variable que almacenara la matriz inversa
    Kinv = [] 
    #Se invierte la matriz K global y se almacena en la matriz Kinv
    Minversa(K, Kinv) 
    #Se multiplica  la K inversa por el arreglo b, y su resultado se almacena en el arreglo T
    productoMxV(Kinv, b, T) 