import psycopg2

conexion= psycopg2.connect(user='postgres',
                 password='avril0212',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor= conexion.cursor()
sentencia=f'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s '
valores=('Cristol','Cantu','mcantu@mail.com', 23 )

cursor.execute(sentencia, valores)
#para guardar el insert en la base de datos usamos conexion.commit() 
#probando me doy cuenta que se guarda sin usarlo
conexion.commit()
registros_actualizados= cursor.rowcount
print (f'Registros actualizados: {registros_actualizados}')
cursor.close()
conexion.close()