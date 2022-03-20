#capitulo 56

#Definimos una funcion que recibe una lista de elementos 
def desplegarNombres(nombres):
    for i in nombres:
        print(i)

nombes = ['Juan', 'Karla', 'Guilly']
desplegarNombres(nombes)
desplegarNombres('Kevin')
#desplegarNombres(10,11) no puede iterar con numeros
#pero si puede con una tupla:
desplegarNombres((10,20))
#lista
desplegarNombres([10,20,30])
