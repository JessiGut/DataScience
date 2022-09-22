# Ejemplo 2
# creamos la clase
class Cliente:
    # creamos la primera clase para inicializar el atributo nombre:
    def inicializar(self, nombre):
        self.nombre = nombre

    # creamos el segundo método
    def imprimir(self):
        # print("Nombre: ", self.nombre)
        return self.nombre

# PRUEBA 1
# bloque principal
# creamos una instancia de la clase Cliente
# (primer objeto)
cliente1 = Cliente()

# era: NombreClase.NombreFuncion
# entonces: NombreInstancia.NombreMétodo
cliente1.inicializar("María")
# el otro método
print("Nombre1: ", cliente1.imprimir())

# PRUEBA 2
# segundo objeto
cliente2 = Cliente()
cliente2.inicializar("Luis")
print("Nombre2: ", cliente2.imprimir())