#capitulo 39

cadena = "Hola"

for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo for \n")

#capitulo 40 Break

for letraa in 'Holii':
    if letraa == 'i':
        print(f'letra encontrada repetida {letraa}')
        break #rompe todo el ciclo
else:
    print("fin")

print("\n")

#capitulo 41 continue

#for i in range(10):
#    if i % 2 == 0:
#        print(f'puro numero para papa: {i}')

for i in range(6):
    if i % 2 != 0:
        continue   #ejecuta la siguiente iteracion es como un skip
    print(f'valores pares: {i}')