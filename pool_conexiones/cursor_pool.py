from conexion import Conexion
from logger_base import logger


class CursorDelPool:
    
    def __init__(self):
        self.__conn= None
        self.__cursor = None
        
    def __enter__(self):
        logger.debug(f'Inicio de with metodo __enter__')
        self.__conn= Conexion.obtener_conexion()
        self.__cursor= self.__conn.cursor()
        return self.__cursor
        
    def __exit__(self, exeption_type, exeption_value, exception_traceback):
        logger.debug(f'Inicio del metodo __exit__')
        if exeption_value:
            self.__conn.rollback()
            logger.error(f'Ocurrio una excepcion {exeption_value}')
        else:
            self.__cursor.close()
            self.__conn.commit()
            logger.debug(f'Commit de la transaccion')
            Conexion.liberar_conexion(self.__conn)
            
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug(f'Listado de personas')
        logger.debug(cursor.fetchall())
   