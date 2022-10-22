#simulacion de sobrecarga de constructores de python
#otras formas de crear objetos en python

class Persona:

    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def persona_con_valores(cls, nombre, apellido):
        return cls(nombre, apellido)
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

persona1 = Persona('Juan', 'Perez')
print(persona1)
persona_vacia = Persona.crear_persona_vacia()
print(persona_vacia)
persona_con_valores = Persona.persona_con_valores('Karla', 'Gomez')
print(persona_con_valores)