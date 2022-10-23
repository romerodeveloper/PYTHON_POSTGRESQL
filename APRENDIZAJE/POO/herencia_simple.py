#ejemplo de herencia simple
from multiprocessing.sharedctypes import Value


class ListaSimple:

    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):

    def __init__(self, elementos=[]):
        super().__init__(elementos)
        #ordenamos siempre los elementos luego ser inicializados
        self.ordenar()
    
    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()

#Lista acepta solo numeros
class ListaEnteros(ListaSimple):

    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        #Una vez validados los elementos, los enviamos a la clase super
        super().__init__(elementos)
    
    def _validar(self, elemento):
        #validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero {elemento}')

    #Sobreescribimos el metodo agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        #Una vez validado lo agregamos a la lista
        super().agregar(elemento)

#lista simple
lista_simple = ListaSimple([5,1,2,6,4,5,3,6])
print(lista_simple)
#lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada) 
lista_ordenada.agregar(-14)
print(lista_ordenada) 
#lista de enteros
lista_enteros = ListaEnteros([1, 3, 4, -15])

#lista de enteros