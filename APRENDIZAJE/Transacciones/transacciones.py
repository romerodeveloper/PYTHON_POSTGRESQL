import psycopg2 as db

conexion = db.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            #una transaccion o ejecuta todas las transacciones de manera correcta o no ejecuta ninguna y se hace roolback
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s,%s,%s)'
            valores = (('Carlos','Lara','clara@mail.com'))
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Juan Carlos','Juarez','jcjuarez@mail.com',1))
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrio un error se hizo un rollback de la transaccion: {e}')
finally: 
    conexion.close()

print('Termino la transaccion, se hizo commit')