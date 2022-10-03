
def Zscore(µ, σ, x):
    return round((x - µ)/ σ, 2)

# EJERCICIO 1

"""
    En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros con una desviación estándar de 0,02 metros. 
    Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. ¿Qué porcentaje de jugadores son más altos que Barnes?
"""

µ = 2.00
s= 0.02
x = 2.03

# print("Zscore Barnes: ", Zscore(µ, s, x))

# Nos vamos a la tabla de Z score: 1.5 --> 0.9332 --> 93.32% son más bajos o igual de altos que Barnes

mas_altos = (1 - 0.9332)*100
# print(mas_altos)

# El 6.68% de los Jugadores son más altos que Barnes.


# EJERCICIO 2

# Chris Paul mide 1,83 metros. ¿Qué proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes?

µ = 2.00
s= 0.02
x = 1.83

# print("Zscore Paul: ", Zscore(µ, s, x))

# El valor es -8.5 --> 0% tiene a ese valor z < -4, estamos ante un Outlier. 93.32% esta entre ellos.


# EJERCICIO 3

"""
    El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve.
    Si el puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve?
"""
porcentaje = 0.9200

# Sabiendo el porcentaje buscaremos en la tabla Z su valor = 1.41


def calculo_x(Z, s, µ):
    return (Z * s) + µ

µ = 55
s= 6
Z = 1.41

# print("Puntuación Steve: ", calculo_x(Z, s, µ))
