# EJERCICIO 1
"""
    1) Crea el siguiente programa:

    Una clase de nombre Librería
    Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería.
    En esta clase Rosalia, crea una función "result" cuyo resultado sea los datos de los libros.
    declara los Objetos siguientes:
    libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
    libro2 --> 33 Botones, Novela negra, Atlantis, 2022
    libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022
"""

class Libreria:

    def __init__(self, nombre, seccion, editorial, año):
        self.nombre = nombre
        self.seccion = seccion
        self.editorial = editorial
        self.año = año

class Rosalia(Libreria):

    def result(self):
        return f"Información del libro en librería 'Rosalia' es {self.nombre}, de la editorial {self.editorial}" +\
               f", cuya sección es {self.seccion}, del año {self.año}"

libro1 = Rosalia('Oceanarium', 'Ciencia', 'Impedimenta', 2021)
libro2 = Rosalia('33 Botones', 'Novela negra', 'Atlantis', 2022)
libro3 = Rosalia('Venganza en Compostela', 'Historia', 'Universo de letras', 2022)

# Descomentar para ejecutar:
# print("1) Información libro 1: ", libro1.result())
# print("2) Información libro 2: ", libro2.result())
# print("3) Información libro 3: ", libro3.result())


# EJERCICIO 2
"""
    2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase,
    define una función de nombre misLibros, cuyo resultado sea los datos de los libros:

    libro4 --> Mi primera Novela, Novela, Bruño, 2019
    libro5 --> Gatos, Literatura, Listado, 2018
"""
class MiLibro(Libreria):

    def misLibros(self):
        return f"Información del libro en librería 'MiLibro' es {self.nombre}, de la editorial {self.editorial}" +\
               f", cuya sección es {self.seccion}, del año {self.año}"

    def get_año(self):
        return self.año

libro4 = MiLibro('Mi primera Novela', 'Novela', 'Bruño', 2019)
libro5 = MiLibro('Gatos', 'Literatura', 'Listado', 2018)

# Descomentar para ejecutar:
# print("4) Información libro 4: ", libro4.misLibros())
# print("5) Información libro 5: ", libro5.misLibros())

# Realiza la media de los años de los libros 4 y 5:

# print(libro4.get_año())

media = (libro4.get_año() + libro5.get_año()) / 2

# Descomentar para ejecutar:
# print("La media de los años es %s" %(media))