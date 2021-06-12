from logging import exception
from psycopg2 import pool
from logger_base import logger


class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'avril0212'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN__CON = 1
    __MAX_CON = 5
    __POOL = None
    
    @classmethod
    def obtener_pool(cls):
        if cls.__POOL is None:
            try:
                cls.__POOL= pool.SimpleConnectionPool(cls.__MIN__CON, 
                                                      cls.__MAX_CON,
                                                      user= cls.__USERNAME,
                                                      password= cls.__PASSWORD,
                                                      host= cls.__HOST,
                                                      port= cls.__DB_PORT,
                                                      database= cls.__DATABASE )
                logger.debug(f"Creacion de pool exitosa {cls.__POOL}")
                return cls.__POOL
            except Exception as e:
                logger.error(f'Error al crear el pool : {e}')
                exit()
        else:
            return cls.__POOL
                
    @classmethod
    def obtener_conexion(cls):
        #obtiene una conexion del pool
        conexion=cls.obtener_pool().getconn()
        logger.debug(f'Conexion realizada desde el pool {conexion}')
        return conexion
    
    @classmethod
    def liberar_conexion(cls, conexion):
        #regresar objeto de conexion del pool
        cls.obtener_pool().putconn(conexion)
        logger.debug(f'Se ha regresado la conexion a su pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__POOL}')
        
    @classmethod
    def cerrar_conexiones(cls):
        #Cerrar el pool y sus conexiones
        cls.obtener_pool().closeall()
        logger.debug(f'Se cerraron todas las conexiones del pool: {cls.__POOL}')
        
            

if __name__ == '__main__':
    conexion_0= Conexion.obtener_conexion()
    conexion_1= Conexion.obtener_conexion()
    conexion_2= Conexion.obtener_conexion()
    
    Conexion.liberar_conexion(conexion_0)
    Conexion.liberar_conexion(conexion_1)
    Conexion.liberar_conexion(conexion_2)
    Conexion.cerrar_conexiones()
    conexion_0= Conexion.obtener_conexion()
    #logger.info(Conexion.obtener_cursor())
    #Conexion.cerrar_conexiones()