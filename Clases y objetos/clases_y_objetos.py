#clase 58,59,60,61,62,63,65

class persona():
    #el metodo init permite agregar atributos y inicializarlos
    def __init__(self, nombre: str, apellido: str, edad: int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #clase 64
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = persona('Juan','Perez',23)
#print(f'Objeto persona 2: {persona1.nombre} {persona1.apellido} {persona1.edad}')
#persona1.mostrar_detalle()
persona.mostrar_detalle(persona1)

persona2 = persona('Karla','Fuentes', 22)
#print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
persona2.mostrar_detalle()