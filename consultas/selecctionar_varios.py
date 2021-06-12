import psycopg2

conexion= psycopg2.connect(user='postgres',
                 password='avril0212',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor= conexion.cursor()
sentencia='SELECT * FROM persona WHERE id_persona IN %s'
entrada = input('Proporciona las pk a s buscar (separadas por comas): ')
tupla= tuple(entrada.split(','))
llaves_primarias = (tupla,) #((1,5,7,4,9),)
cursor.execute(sentencia, llaves_primarias)
registros= cursor.fetchall()
for registro in registros:
    print (registro)
cursor.close()
conexion.close()
