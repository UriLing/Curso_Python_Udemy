#Video 30
nombre=input("Nombre del libro ")
id_libro=int(input("Dame la ID " ))
precio=float(input("Precio "))
Envio=(input("Verdadero o falso? "))

if Envio == 'True':
    Envio=True
else:
    Envio=False

print(f""""
    Nombre: {nombre} 
    id: {id_libro}
    precio= {precio}
    Envio gratuito?: {Envio}
""")

