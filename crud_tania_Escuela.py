import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="tania_Escuela"    
    )

    if conexion.is_connected():
        print("¡Conectado exitosamente a tania_Escuela!")
        cursor = conexion.cursor()

except Error as e:
    print(f" Error de conexión: {e}")
    exit()

def crear_estudiante(nombre, edad):
    try:
        sql = "INSERT INTO Estudiantes (nombre, edad) VALUES (%s, %s)"
        valores = (nombre, edad)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f" {cursor.rowcount} estudiante agregado: {nombre}")
    except Error as e:
        print(f" Error al agregar: {e}")

def ver_estudiantes():
    try:
        cursor.execute("SELECT * FROM Estudiantes")
        resultado = cursor.fetchall()
        print("\n" + "="*40)
        print(" Lista de Estudiantes:")
        print("-"*40)
        if not resultado:
            print("   No hay registros aún")
        else:
            for fila in resultado:
                print(f"   ID: {fila[0]} | Nombre: {fila[1]} | Edad: {fila[2]}")
        print("="*40 + "\n")
        return resultado
    except Error as e:
        print(f" Error al consultar: {e}")

def actualizar_estudiante(id_estudiante, nuevo_nombre=None, nueva_edad=None):
    try:
        if nueva_edad:
            sql = "UPDATE Estudiantes SET edad = %s WHERE id = %s"
            valores = (nueva_edad, id_estudiante)
        elif nuevo_nombre:
            sql = "UPDATE Estudiantes SET nombre = %s WHERE id = %s"
            valores = (nuevo_nombre, id_estudiante)
        else:
            print(" No distes nada para actualizar")
            return

        cursor.execute(sql, valores)
        conexion.commit()
        print(f" {cursor.rowcount} registro actualizado (ID: {id_estudiante})")
    except Error as e:
        print(f"Error al actualizar: {e}")
def eliminar_estudiante(id_estudiante):
    try:
        sql = "DELETE FROM Estudiantes WHERE id = %s"
        valores = (id_estudiante,)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f" {cursor.rowcount} registro eliminado (ID: {id_estudiante})")
    except Error as e:
        print(f"Error al eliminar: {e}")
        if __name__ == "__main__":
             print("\n--- 🎓 SISTEMA DE GESTIÓN DE ESTUDIANTES ---")

    
    crear_estudiante("Ana", 20)
    crear_estudiante("Luis", 22)
    crear_estudiante("María", 19)
    ver_estudiantes()
    actualizar_estudiante(1, nueva_edad=21)
    ver_estudiantes()
    eliminar_estudiante(2)
    ver_estudiantes()
    cursor.close()
    conexion.close()
    print(" Conexión cerrada. ¡Fin del programa!")

