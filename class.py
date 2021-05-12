from banco import *

#atributos y funciones a utilizar
class item():
    _id = 0
    _x = 0.0
    _node1 = 0
    _node2 = 0
    _value = 0

    def __init__(self):
        pass

    def getId(self):
        return self._id

    def getX(self):
        return self._x

    def getNode1(self):
        return self._node1

    def getNode2(self):
        return self._node2

    def getValue(self):
        return self._value


#elemento de una malla
class elementm(item):
    def setIntIntInt(self, identifier, firstnode, secondnode):  #valores de los nodos, y el identificador del elemento.
        self._node1 = firstnode
        self._node2 = secondnode
        self._id = identifier

#nodo de una malla
class nodem(item):
    def setIntFloat(self, identifier, x_coordinate):#el id y la coordenada de x
        self._id = identifier
        self._x = x_coordinate



#condiciones de contorno, nodo en que se aplica la condicion ya sea Neumann o en Dirichlet y el identificador del elemento
class condiciones(item):
    def setIntFloat(self, node_to_apply, prescribed_value):
        self._node1 = node_to_apply
        self._value = prescribed_value

#malla de  la ecuacion de Poisson
class mesh():
    __parameters = []
    __sizes = []
    __node_list = []
    __element_list = []
    __dirichlet_list = []
    __neumman_list = []

    def __init__(self):
        pass

    #parametros los valores de l, k y Q
    def setParameters(self, l, k, Q):
        self.__parameters.insert(PARAMETERS['ELEMENT_LENGHT'], l)
        self.__parameters.insert(PARAMETERS['THERMAL_CONDUCTIVITY'], k)
        self.__parameters.insert(PARAMETERS['HEAT_SOURCE'], Q)

    # numero de nodos, elementos de la malla, condiciones de dirichlet y condiciones de neumann
    def setSizes(self, nnodes, neltos, ndirich, nneu):
        self.__sizes.insert(SIZES['NODES'], nnodes)
        self.__sizes.insert(SIZES['ELEMENTS'], neltos)
        self.__sizes.insert(SIZES['DIRICHLET'], ndirich)
        self.__sizes.insert(SIZES['NEUMANN'], nneu)

    #listas a utilizar en el objeto mesh, y objetos que estos almacenaran.
    def createData(self):
        for i in range(self.__sizes[SIZES['NODES']]):
            self.__node_list.append(nodem())
        for i in range(self.__sizes[SIZES['ELEMENTS']]):
            self.__element_list.append(elementm())
        for i in range(self.__sizes[SIZES['DIRICHLET']]):
            self.__dirichlet_list.append(condiciones())
        for i in range(self.__sizes[SIZES['NEUMANN']]):
            self.__neumman_list.append(condiciones())

    
#Getters a utilizar para la clase mesh

    def getSize(self, i):
        return self.__sizes[i]

    def getParameter(self, i):
        return self.__parameters[i]

    def getNodes(self):
        return self.__node_list

    def getElements(self):
        return self.__element_list

    def getDirichlet(self):
        return self.__dirichlet_list

    def getNeumann(self):
        return self.__neumman_list

    def getNode(self, i):
        return self.__node_list[i]

    def getElement(self, i):
        return self.__element_list[i]

    def getCondition(self, i, type):
        if type == SIZES['DIRICHLET']:
            return self.__dirichlet_list[i]
        else:
            return self.__neumman_list[i]