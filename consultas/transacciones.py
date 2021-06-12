import psycopg2

conexion= psycopg2.connect(user='postgres',
                 password='avril0212',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

try:
    cursor= conexion.cursor()
    sentencia=f'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s '
    valores=('Cristobal','Colon','ccolon@mail.com', 23 )
    cursor.execute(sentencia, valores)
    
    sentencia=f'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
    valores=('Herculesito','Gimenez','Herculito@mail.com')
    cursor.execute(sentencia, valores)
    #para guardar el insert en la base de datos usamos conexion.commit() 
    #probando me doy cuenta que se guarda sin usarlo
    conexion.commit()   
except Exception as e:
    conexion.rollback() #hace rollback en caso de error
    print (type (e))
    print (f'ocurrio un error {e}')
finally:    
    cursor.close()
    conexion.close()