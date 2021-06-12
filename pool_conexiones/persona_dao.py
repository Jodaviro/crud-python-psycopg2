from cursor_pool import CursorDelPool
from persona import Persona
from logger_base import logger


class PersonaDao:
    ''' DAO (Data Acces Objetc) CRUD (Create-Read-Update-Delete)'''
    __SELECCIONAR= f'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR= f'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    __ACTUALIZAR= f'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona= %s'
    __ELIMINAR= f'DELETE FROM persona WHERE nombre= %s AND apellido= %s '
    
    
    @classmethod
    def selecionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros= cursor.fetchall()
            personas= []
            for registro in registros:
                persona= Persona(registro[0], registro[1], registro[2],registro[3] )
                personas.append(persona)
            return personas
        
    
    @classmethod
    def insertar(cls, persona):

        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar {persona}')
            values= (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, values)
            return cursor.rowcount
        
    
    @classmethod    
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar {persona}')
            values= (persona.get_nombre(), persona.get_apellido())
            cursor.execute(cls.__ELIMINAR, values)
            return cursor.rowcount

            
    @classmethod
    def actualizar (cls,persona):
        with CursorDelPool() as cursor:
  
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar {persona}')
            values= (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, values)
            return cursor.rowcount
            
            
        

if __name__ == '__main__':

    
    #seleccionar
    personas=PersonaDao.selecionar()   
    for persona in personas:
        logger.debug(persona)
        #logger.debug(persona.get_id_persona())
    
    
    
    
    #Eliminar
    # persona= Persona (nombre= 'Vicente', apellido='Fernande')
    # personas_insertadas= PersonaDao.eliminar(persona)
    # logger.debug(f'Persona eliminada: {personas_insertadas}')
    
     #Insertar
    # persona= Persona (nombre= 'Nieves', apellido='Rodriguez', email='nievesrodriy@mail')
    # personas_insertadas= PersonaDao.insertar(persona)
    # logger.debug(f'Persona insertar: {personas_insertadas}')
    
    #actualizar
    # persona= Persona(id_persona= 48,nombre= 'Vicente', apellido='Fernande', email='Vfernandez@mail')
    # personas_insertadas= PersonaDao.actualizar(persona )
    # logger.debug(f'Persona actualizada: {personas_insertadas}')
    