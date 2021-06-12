import psycopg2

conexion= psycopg2.connect(user='postgres',
                 password='avril0212',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor= conexion.cursor()
sentencia=f'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
valores=(
        ('Marcos','Cantu','mcantu@mail.com'),
        ('Jose','Gonzales','gonzalez@mail.com'),
        ('Carlos','Quintana','Cquintana@mail.com'),
        ('David','Rodriguez','drodriguez@mail.com')

 )

cursor.executemany(sentencia, valores)
#para guardar el insert en la base de datos usamos conexion.commit() 
#probando me doy cuenta que se guarda sin usarlo
conexion.commit()
registros_insertados= cursor.rowcount
print (f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()