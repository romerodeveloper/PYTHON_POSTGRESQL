from logger_base import log
from conexion import Conexion 

class CursorDelPool:

    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with')
        self._conn = Conexion.ObtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Estamos en el metodo exit')
        if valor_excepcion:
            self._conn.rollback()
            log.debug(f'se produjo un error de tipo {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conn.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.LiberarConexion(self._conn)
