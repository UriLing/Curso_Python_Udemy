#capitulo 47
#Set es una coleccion sin orden y sin indices (no puede haber valores repetidos)

planetas = {'marte','jupiter','venus'}
print(planetas)
#largo
print(len(planetas))
#revisar si un objeto existe en la coleccion
print('marte' in planetas)
#agregar elementos
planetas.add('tierra')
print(planetas)
#no se puede duplicar elementos
planetas.add('tierra')
print(planetas)
#eliminar elementos
planetas.remove('tierra')
print(planetas)
#eliminar elemento sin que de errores en caso de no encontrarlo
planetas.discard('jupiters')
print(planetas)
#limpiar todos los elementos
planetas.clear()
print(planetas)
#eliminar el set() por completo
del planetas