import sqlite3 as sql3

class BDD:
    def __init__(self, n_BDD='BDD\\BaseBDD.db'):
        self.conexion = sql3.connect(n_BDD)
        self.cursor = self.conexion.cursor()
        
    def crear_BDD(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Libros("+
            "id integer primary key autoincrement,"+
            "Libro string,"+
            "Anio_Publicacion int(255),"+
            "Autor string,"+
            "Descripcion string"+
            ")"
        )
        self.conexion.commit()
        self.cerrar()
    
    def nuevo_R(self, Libro:str,F_Publicacion:int,Autor:str,Descripcion:str):
        """
        Agregar Un Nuevo Libro Al Registro, Los Argumentos Que Recibe La Funcion Son:\n
        Libro: Nombre Del Libro (Tipo Cadena)\n
        F_Publicacion: Especificar Año De Publicacion De La Obra (Tipo Entero)\n
        Autor: Nombre Del Autor De La Obra\n
        Descripcion: Breve Descripcion Acerca De La Obra\n
        """
        try:
            self.cursor.execute("INSERT INTO Libros (Libro,Anio_Publicacion,Autor,Descripcion) VALUES (?,?,?,?)",(Libro,F_Publicacion,Autor,Descripcion))
            self.conexion.commit()
            self.cerrar()
        except:
            print("Error Al Registrar Datos\n")
            self.cerrar()
            
        
 
    def ver_Datos(self) -> list:
        """
        Funcion Para Visualizar Datos Almacenados En BDD\n
        Imprime Los Elementos Almacenados
        """
        self.cursor.execute("SELECT * FROM Libros;")
        datos = self.cursor.fetchall()
        #Formato Para Imprimir En Consola Los Datos Almacenados
        for i in datos:
            print("-"*10)
            print("ID: ", i[0])
            print("Libro: ",i[1])
            print("Autor: ",i[3])
            print("Publicacion: ",i[2])
            print("Descripcion: ", i[4])
            print("-"*10)
        
        self.cerrar()
        return datos

    def cerrar(self):
        """
        Funcion Que Cierra La Conexión Con La BDD
        """
        try:
            self.conexion.close()
        except:
            print("Error Al Cerrar La Conexion \n")