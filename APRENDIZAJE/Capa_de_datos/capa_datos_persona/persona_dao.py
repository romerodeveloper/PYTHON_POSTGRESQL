from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'persona insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'persona actualizada: {persona}')
                return cursor.rowcount 

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona, )
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'persona eliminada: {persona}')
                return cursor.rowcount 


if __name__ == '__main__':
    #insertar un registro
    #persona1 = Persona(nombre='pedro', apellido='najera', email='pnajera@gmail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'personas insertadas {personas_insertadas}')
    
    #actualizar un registro
    #persona1 = Persona(1, 'juan', 'perez', 'jperez@gmail.com')
    #persona_actualizada = PersonaDAO.actualizar(persona1)
    #log.debug(f'personas insertadas {persona_actualizada}')

    #Eliminar registro
    persona1 = Persona(id_persona=12)
    persona_eliminada = PersonaDAO.eliminar(persona1) 
    log.debug(f'Personas eliminadas: {persona_eliminada}')

    #seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

        