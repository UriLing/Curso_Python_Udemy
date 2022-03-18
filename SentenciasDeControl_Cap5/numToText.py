#Capitulo 33

num = int(input("Escribe un valor"))
numText = ""

if num == 1:
    numText = 'Numero 1'
elif num == 2:
    numText = 'Numero 2'
elif num == 3:
    numText = 'Numero 3'
else:
    numText = 'Valor desconocido'

print(f'El número es: {num}, {numText}')

#condicion ternaria
#print("hola") if condicion else print("esto es falso")