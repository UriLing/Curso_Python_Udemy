#clase 42

nombres = ['juan','karla','jacc','gonzalo']
#clase 42

nombres = ['Jose', 'Yessi','Jacc','Gonzalo']

#imprime la lista
print(nombres)
#imprime un objeto de la lista
print(nombres[2])
print(nombres[1])
#acceder a los valores de la lista de manera inversa
print(nombres[-2])
print(nombres[-3])

#clase 43
print("\n")

#imprimimos un rango
print(nombres[0:2])
#ir del inicio al indice (sin incluirlo)
print(nombres[:3])
#desde el indice indicado hasta el final de la lista
print(nombres[1:])
#cambiamos un valor especificando un indice 
nombres[0] = 'Saul'
print(nombres)
#iterar la lista
for i in nombres:
    print(i)
else:
    print('no hay mas nombres en la lista')

#clase 44
print('\n')

#preguntar el largo de una lista
print(len(nombres))
#agregar un elemento
nombres.append('Chocotorro')
print(nombres)
#insertar un elemento en un indice en especifico
nombres.insert(4,'Gansito')
#los elementos se moveran a la derecha si el nuevo elemento entra
print(nombres)
#remover un elemento de la lista
nombres.remove('Gansito')
print(nombres)
#remover el ultimo valor agregado a la lista
nombres.pop()
print(nombres)
#eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)
#limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
#eliminar la lista por completo de la memoria
del nombres     #aqui mandara un error por que no puede acceder

