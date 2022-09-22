class Cliente:
    
    def __init__(self, Id, nombre, edad, estado_civil, profesion):
        self.Id = Id
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil
        self.profesion = profesion
        
    def metodo_1():
        print("aqui creo el contenido del método 1")
        
    def metodo_2():
        print("aqui creo el contenido del método 2")

cliente1 = Cliente(1, "Juan", 30, "soltero", "ingeniero")
cliente2 = Cliente(2, "María", 45, "casada", "arquitecta")
cliente3 = Cliente(3, "Carlos", 25, "soltero", "abogado")


Cliente.metodo_1()
Cliente.metodo_2()