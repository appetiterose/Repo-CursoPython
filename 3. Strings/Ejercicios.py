'''Ejercicio 1
Crear un programa que tenga una variable con la cadena "Te quiero
solo como amigo", y muestre la siguiente infomación:
- Imprima los dos primeros caracteres.
- Imprima los tres últimos caracteres.
- Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena
fuera "recta" deberia imprimir rca
- Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola
mundo! debe imprimir !odnum aloh
- Imprima la cadena en un sentido y ensentido inverso. Ej.: Si la
cadena es "reflejo" imprime reflejoojelfer'''
print('Ejercicio 1')

cadena1 = 'Te quiero solo como amigo'
print('Primeros 2 caracteres:', cadena1[0 : 2])
print('Ultimos 3 caracteres:', cadena1[-3 : ])
print('Cadena cada 2 caracteres:', cadena1[: : 2])
print('Cadena en sentido inverso:', cadena1[: : -1])
print('Cadena un sentido e inverso:', cadena1 + cadena1[: : -1])

'''Ejercicio 2
Crear un programa que tenga una variable con la cadena "Separado"
y un carácter de coma (,); e inserte el carácter entre cada letra
de la cadena. Ej: seperar y, deberia devolver s,e,p,a,r,a,r
pista: utilizar el método "Replace" '''
print('\nEjercicio 2')

cadena2 = 'eperado'
cadena3 = ','
reemplazar = cadena2.replace("", cadena3)
print('S'+ reemplazar)