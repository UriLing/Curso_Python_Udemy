#clase 48
#Un diccionario esta compuesto por 2 elementos (key, value)
diccionario = {
    'IDE' : 'Integrated Develoment Enviroment',
    'OOP' : 'Object Oriented Programming' ,
    'DBMS' : 'Database Managment System'
}

print(diccionario)
#largo
print(len(diccionario))
#buscar un elemento con su llave
print(diccionario['IDE'])
#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#modificar elementos en un diccionario 
diccionario['IDE'] = 'integrated develoment enviroment'
print(diccionario)

#clase 49
print('\n')
#recorrer todo el diccionario
for llave, valor in diccionario.items():
    print(llave, valor)
#recorrer unicamente los llaves
print('\n')
for llave in diccionario.keys():
    print(llave)
print('\n')
#recorrder unicamente los valores
for valor in diccionario.values():
    print(valor)
#comprobar existencia de algun elemento
print('IDE' in diccionario)
#agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
#remover un elemento
diccionario.pop('DBMS')
print(diccionario)
#limpiar el diccionario
diccionario.clear()
print(diccionario)
#eliminar el diccionario por completo
del diccionario