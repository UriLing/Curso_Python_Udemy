#video35
mes = int(input('Dame el numero del mes(1-12): 2'))

estacion = None
#None == Null
if estacion == 1 or 2 or 12:
    estacion = 'Invierno'
elif estacion == 3 or 4 or 5:
    estacion = 'Primavera'
elif estacion == 6 or 7 or 8:
    estacion == 'Verano'
elif estacion == 9 or 10 or 11:
    estacion == 'Otoño'
else:
    print("Error, no hay más de 12 meses en el año")
print(f'Para el mes de {mes} la estacion es {estacion}')