#Video 36 y 37

edad = int(input("Introduce tu edad correspondiente: "))

if edad >=0  and edad <10:
    mensaje="La infancia es increible..."
elif edad >=10 and edad <20:
    mensaje="Muchos cambios y mucho estudio..."
elif edad >=20 and edad <=30:
    mensaje="Amor y comienza el trabajo"
else:
    print("Etapa de vida no reconocida de momento")
print(f'Tu edad es {edad}, {mensaje}')