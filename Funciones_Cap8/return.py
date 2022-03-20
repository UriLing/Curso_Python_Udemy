#clase 52
def suma(a,b) -> int:
    return a + b

resultado = suma(5,3)
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de otra suma es:',suma(9,1))

#clase 53
def suma2(c = 0,d= 0) -> int:
    return c + d

print(f'\n La suma con los valores definidos es {suma2(10,10)}')