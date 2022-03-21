#clase 72

class persona():
    
    def __init__(self, nombre: str, apellido: str, edad: int, *tupla, **diccionario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.tupla = tupla
        self.diccionario = diccionario

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.tupla} {self.diccionario}')

persona1 = persona('Juan','Perez',23, 1,2,5,78, m= 'Mariscos', r= 'Resina')
persona.mostrar_detalle(persona1)

persona2 = persona('Karla','Fuentes', 22)
persona2.mostrar_detalle()