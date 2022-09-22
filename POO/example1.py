class Empleado:
    # funciones se les llama MÉTODOS
    # variables se les atributos
    def __init__(self, Id, Name, Age, Role):
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.Role = Role

# Instancia
# genero tantos clientes/empleado como quiera de esta forma
# empleado1 es el objeto1

empleado1 = Empleado(1, "Ana", 30, "ingeniera")
empleado2 = Empleado(2, "Pedro", 45, "arquitecto")
empleado3 = Empleado(3, "Andrea", 25, "abogada")

print(empleado1.Age)
print(empleado2.Name)
print(empleado3.Role)
