from dataclasses import dataclass
import psycopg2

#creacion del objeto conexion
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        #objeto que permitira ejecutar sentencias SQL en postgres
        with  conexion.cursor() as cursor:
            #%s significa placeholder parametro posicional
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            #llaves_primarias = ((1,2,3,4),)
            entrada = input('Proporciona los id\ ´s a buscar(separados por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            #asignacion de sentencia a ejecutar, le enviamos una tupla con el id para identificar el placeholder
            cursor.execute(sentencia, llaves_primarias)
            #fetchone permite recuperar el registro de la sentencia que se ha ejecutado
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally: 
    #cerrar conexion
    conexion.close()
