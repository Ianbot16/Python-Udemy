import mysql.connector
#Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Master_python"
)

#La conexión ha sido correcta
#print(database)
cursor = database.cursor(buffered=True)

#Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS Master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
    
#Crear tablas
cursor.execute("""
               CREATE TABLE IF NOT EXISTS Vehiculos(
                   id int(10) auto_increment not null,
                   marca varchar(40) not null,
                   modelo varchar(40) not null,
                   precio float(10,2) not null,
                   CONSTRAINT pk_vehiculo PRIMARY KEY(id)
               )
               """)

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#cursor.execute("INSERT INTO Vehiculos VALUES(null,'Opel','Astra',18500)")
coches=[
    ("Seat","Ibiza",5000),
    ("Renault","Clio",15000),
    ("Citroen","Saxo",2000),
    ("Mercedes","Clase C",35000)
]

#cursor.executemany("INSERT INTO Vehiculos VALUES(null,%s,%s,%s)", coches)

database.commit()

cursor.execute("SELECT * FROM Vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
result= cursor.fetchall()

print("-----TODOS MIS COCHES-----")
for coche in result:
    print(coche[1], ":",coche[3])
    
cursor.execute("SELECT * FROM Vehiculos")
result=cursor.fetchone()

print(coche)

#Borrar
cursor.execute("DELETE FROM Vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount,"borrada/as.")

#Actualizar
cursor.execute("UPDATE Vehiculos SET modelo='León' WHERE marca='Seat'")
database.commit()

print(cursor.rowcount, "actualizada/as.")