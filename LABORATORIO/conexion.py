from logger_base import log
from psycopg2 import pool
import sys

class Conexion:

    #Declaracion de variables de la base
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT =  '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try: 
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                    host = cls._HOST,
                                                    port = cls._DB_PORT,
                                                    database = cls._DATABASE,
                                                    user = cls._USERNAME,
                                                    password = cls._PASSWORD
                                                    )
                log.debug(f'Se creo el pool de forma exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'A ocurrido un error en el pool {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def ObtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f'Se creo la conexion de forma exitosa {conexion} ')
        return conexion

    @classmethod
    def LiberarConexion(cls, conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f'Se libero la conexion de forma correcta {conexion}')

            