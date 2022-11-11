'''Ejercicio 1
Crear un programa que pida al usuario una letra y si es vocal
muestre el mensaje "Es vocal". Sino, decirle al usiario que no es
vocal'''
letra = input('Ingresa una letra: ')

if letra.lower() == 'a':
    print('Ingresaste una vocal y es la "A"')
elif letra.lower() == 'e':
    print('Ingresaste una vocal y es la "E"')
elif letra.lower() == 'i':
    print('Ingresaste una vocal y es la "I"')
elif letra.lower() == 'o':
    print('Ingresaste una vocal y es la "O"')
elif letra.lower() == 'u':
    print('Ingresaste una vocal y es la "U"')
else:
    print('Lo que ingresaste no corresponde a una vocal')

'''Ejercicio 2
Escribir un programa que, dado un número entero, muestre su
valor absoluto. Nota: para los números positivos su valor absoluto
es igual al número (el valor absoluto de 52 es 52), mientras que,
para los negativos, su valor absoluto es el número multiplicado
por -1 (el valor absoluto de -52 es 52)'''
numero = int(input('Ingresa un valor entero: '))

if numero > 0:
    print('El valor absoluto es: ', numero)
else:
    print('El valor absoluto es: ', numero*-1)