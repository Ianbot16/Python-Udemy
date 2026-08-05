#importar modulo
import sqlite3

#Conexión
conexion = sqlite3.connect("19-Base_de_datos/Pruebas.db")

#Cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS Productos (
               Id INTEGER PRIMARY KEY AUTOINCREMENT not null,  
               Titulo varchar(255),
               Descripcion text,
               Precio int(255) ); """)

#Guardar cambios
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO Productos VALUES (null, 'Segundo producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

#Borrar registros
cursor.execute("DELETE FROM Productos")
conexion.commit()

#Insertar muchos regstros de golpe
productos = [
    ("Ordenador portatil","Buen PC",700),
    ("Telefono movil","Buen telefono",140),
    ("Placa base","Buena base",80),
    ("Tablet 15","Buen PC",300)
]
cursor.executemany("INSERT INTO Productos VALUES(null,?,?,?)", productos)
conexion.commit()

#Update
cursor.execute("UPDATE Productos SET Precio = 150 WHERE Precio = 80")

#Listar datos
cursor.execute("SELECT * FROM Productos WHERE Precio >= 50;")
productos = cursor.fetchall()

for producto in productos:
    print("Titulo: ",producto[1])
    print("Descripcion: ",producto[2])
    print("Precio: ",producto[3])
    print("\n")  

#Cerrar conexión
conexion.close()