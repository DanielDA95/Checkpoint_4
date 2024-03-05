# Primero
lista = ['beta', 'delta', 'gama', 'alfa']
tupla = (4,5,6)
flotante = 29.36
entero = 1995
diccionario = {'nombre' : 'Daniel', 'edad' : '28', 'ciudad' : 'Bilbao'}

from decimal import Decimal
numero_decimal = 5.12

#Segundo punto 
import math
print(math.ceil(flotante))

#Tercer punto
print(math.sqrt(entero))

# Cuarto punto
print(diccionario['nombre'])

# Quinto Punto
print(tupla[1])

#Sexto punto
lista = ['beta', 'delta', 'gama', 'alfa']
lista.extend(['foxtrot'])
print(lista)

#Septimo punto
lista[0] = 'zulu'
print(lista)

# Octavo punto
lista.sort()
print(lista)

#Noveno punto 
tupla = (4,5,6)
tupla += (16, )
print(tupla)
