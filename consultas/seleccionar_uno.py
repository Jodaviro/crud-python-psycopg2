import psycopg2

conexion= psycopg2.connect(user='postgres',
                 password='avril0212',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor= conexion.cursor()
sentencia='SELECT * FROM persona WHERE id_persona = %s'
id_persona = 6
llave_primaria= (id_persona,)
cursor.execute(sentencia, llave_primaria)
registros= cursor.fetchone()
print (registros)
cursor.close()
conexion.close()