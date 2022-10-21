from telnetlib import PRAGMA_HEARTBEAT


cadena = 'Estoy utilizando los metodos de Python'
cadena2 = 'ESTOY UTILIZANDO LOS METODOS DE PYTHON'
cadena3 = 'estoy utilizando los metodos de Python'
cadena4 = 'Estoy utIlizando lOs metoDos de Python'

print(cadena2.lower()) #Cambia mayusculas a minusculas
print(cadena.upper()) #Inverso de lower
print(cadena3.capitalize()) #Cambia la primer letra a mayuscula
print(cadena3.title()) #Cambia cada inicial de palabra a mayuscula
print(cadena4.swapcase()) #Cambia minusculas a mayusculas y viceversa