#clase 45

"""
Una tupla es como un arreglo pero es inmutable
por lo tanto no se puede modificar
"""
#definimos la tupla
frutas = ('naranja', 'platano', 'guayaba')
#largo de la tupla
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a un rango (sin incluir el ultimo)
print(frutas[0:1])  #cuando una tupla solo tiene un elemento tendra un ","

#clase 46
print("\n")

#recorrer elementos
for fruta in frutas:
    print(fruta, end= ' ')
#cambiar el valor de una tupla (Esto no se suele hacer pues es una mala practica)
frutList = list(frutas)
frutList[0] = 'pera'
frutas = tuple(frutList)
print('\n',frutas)
#eliminar la tupla por completo
del frutas