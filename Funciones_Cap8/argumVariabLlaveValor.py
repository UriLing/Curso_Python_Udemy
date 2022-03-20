#clase 55

#creamos el diccionario variable
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE = 'Integrated Delovepment Enviroment', PK = 'Primary Key')
