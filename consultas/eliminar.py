import psycopg2

conexion= psycopg2.connect(user='postgres',
                 password='avril0212',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor= conexion.cursor()
sentencia=f'DELETE FROM persona WHERE id_persona = %s'
valores=(7,)
cursor.execute(sentencia, valores)
#para guardar el insert en la base de datos usamos conexion.commit() 
#probando me doy cuenta que se guarda sin usarlo
conexion.commit()
registros_eliminados= cursor.rowcount
print (f'Registros eliminados: {registros_eliminados}')
cursor.close()
conexion.close()