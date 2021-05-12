from banco import *
from class import *
from readfile import *
from SEL import *


#Se llaman  las matrices a utilizar
localKs = []
localbs = []

K = []
b = array('f')
T = array('f')

print("--------MEF 1D--------")
print("Transferencia de calor")

#Se crea el archivo mesh
d = mesh()
#Se leen los elementos del archivo de texto y se almacenan en sus correspondientes variables dentro de la malla m
leermalla(d)
#Se crean los sistemas locales en base a la informacion leida y se muestra
crearSistemasLocales(d, localKs, localbs)
muestraKs(localKs); muestraBs(localbs)
#Se incializan las matrices con ceros y luego se ejecuta el ensamblaje
matrixcero(K, d.getSize(SIZES['NODES']))
arraycero(b, d.getSize(SIZES['NODES']))
ensamblaje(d, localKs, localbs, K, b)

#Se aplican las condicones de Neumann al arreglo b
Neumann(d, b)
# showArray(b)
# print("NEUMANN\n")

#Se aplican las condiciones de Dirichlet al sistema de ecuaciones
Dirichlet(d, K, b)
# showMatrix(K)
# print("")
# showArray(b)
# print("Dirichlet\n")

#Se inicializa el arreglo T en ceros, con una longitid igual a la del arreglo b
arraycero(T, len(b))

# showArray(T)
# print("")

#Se calcula el resultado del sistema de ecuaciones Kb = T
calculo(K,b,T)

#Se muestra el resultado final del modelo
muestraArray(T)