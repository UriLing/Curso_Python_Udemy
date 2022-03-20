#clase 54

#creamos una funcion que recibe como parametros los valores de una tupla
def listarNombres(*nombres):    #se antepone el '*' por que no sabemos cuantos parametros recibiremos
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Marifer', 'Judy', 'Jesus')