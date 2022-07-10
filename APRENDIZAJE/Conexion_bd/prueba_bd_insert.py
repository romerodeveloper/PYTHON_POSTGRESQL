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
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                    ('Marcos', 'Cantu', 'mcantu@mail.com'),
                    ('Angel', 'Quintana', 'aquintana@mail.com'),
                    ('Maria', 'Gonzales', 'mgonzalez@mail.com')
            )
            #el executemany lo que hace es ejecutar varios datos
            cursor.executemany(sentencia, valores)
            #conexion.commit() se usa para guardar los cambios a la base de datos, pero no se requiere cuando se usa with
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally: 
    #cerrar conexion
    conexion.close()