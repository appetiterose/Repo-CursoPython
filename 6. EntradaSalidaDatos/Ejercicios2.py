'''Ejercicio 1
Escribir un programa que solicite al usuario un vocal en
minuscula, y luego una letra en mayúsculas. El programa debe
convertir la letra en minúscula y la vocal en mayúscula, y al
final deben ser concatenadas ambas'''
vocal = input('Ingresa una vocal en minuscula: ')
letra = input('Ingresa cualquier letra en mayúscula: ')

print('Resultado\nVocal:', vocal.upper(), 'Letra:', letra.lower())

'''Ejercicio 2
Hacer un programa que pida al usuario su nombre, su edad y su
sexo y lo muestre de la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>'''

nombre = input('Ingresa tu nombre(s): ')
edad = int(input('Ingresa tu edad: '))
sexo = input('Hombre o Mujer?: ')

print('Te llamas: {}\nTu edad es: {} años\nEres: {}'.format(nombre, edad, sexo))