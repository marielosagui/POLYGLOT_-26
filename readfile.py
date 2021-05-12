from class import *
import os

# funciones que ayudaran a leer los datos de un archivo de texto y almacenar.

def obtener_datos(file, nlineas, n, mode, item_list):
    x = file.readline()
    x = file.readline()
    if nlineas == LINES['DOUBLELINE']:
        x = file.readline()
    for i in range(n):
        if mode == MODES['INT_FLOAT']:
            arr = file.readline().split()
            e = int(arr[0]); r = float(arr[1])
            item_list[i].setIntFloat(e, r)
        elif mode == MODES['INT_INT_INT']:
            arr = file.readline().split()
            e1 = int(arr[0]); e2 = int(arr[1]); e3 = int(arr[2])
            item_list[i].setIntIntInt(e1,e2,e3)

def leermalla(m):
    while True:
        filename = input('Ingrese el nombre del archivo: ')
        if os.path.isfile(filename) == True:
            break
    file = open(filename)
    arr = file.readline().split()
    l = float(arr[0]); k = float(arr[1]); Q = float(arr[2])
    arr = file.readline().split()
    n_nodes = int(arr[0]); n_elementos = int(arr[1]); n_dirich = int(arr[2]); n_neumann = int(arr[3])

    m.setParameters(l,k,Q)
    m.setSizes(n_nodes, n_elementos, n_dirich, n_neumann)
    m.createData()
    
    obtener_datos(file, LINES['SINGLELINE'], n_nodes, MODES['INT_FLOAT'], m.getNodes())
    obtener_datos(file, LINES['DOUBLELINE'], n_elementos, MODES['INT_INT_INT'], m.getElements())
    obtener_datos(file, LINES['DOUBLELINE'], n_dirich, MODES['INT_FLOAT'], m.getDirichlet())
    obtener_datos(file, LINES['DOUBLELINE'], n_neumann, MODES['INT_FLOAT'], m.getNeumann())

    file.close()