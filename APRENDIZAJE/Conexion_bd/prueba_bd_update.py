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
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona=%s'
            #Para actualizar un solo dato
            #valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com',1)
            #cursor.execute(sentencia, valores)
            #Para actualizar varios datos
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com',1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com',2)
            )
            cursor.executemany(sentencia, valores)
            
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally: 
    #cerrar conexion
    conexion.close()