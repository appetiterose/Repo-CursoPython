'''Escribe un programa que pida dos palabras y diga si riman o no.
Si coiciden las tres últimas letras tiene que decir que riman. Si
coinciden sólo las dos últimas tiene que decir que riman un poco
y si no, que no riman'''
word1 = input('Introduce una palabra: ')
word2 = input('Introduce otra palabra: ')

if len(word1) < 3 or len(word2) < 3:
    print('No riman por que tienen menos de 3 letras')
elif word1[-3 : ] == word2[-3 : ]:
    print('Las palabras riman')
elif word1[-2 : ] == word2[-2 : ]:
    print('Las palabras riman un poco')
else:
    print('Las palabras no riman')

'''Crear un programa que permita al usuario elegir un candidato por
el cual votar. Las posibilidades son: candidato A por el partido
rojo, candidato B por el partido verde, candidato C por el partido
azul. Según el candidato elegido (A, B ó C) se le debe imprimir el
mensaje "Usted ha votado por el partido xx".
Si el usuario ingresa una opción que no corresponde a ninguno
de los candidatos disponibles, indicar "Opción errónea".'''
voto = input('¿Por cual candidato desea votar? (A. B ó C): ')

if voto.upper() == 'A':
    print('Usted ha votado por el partido ROJO')
elif voto.upper() == 'B':
    print('Usted ha votado por el partido VERDE')
elif voto.upper() == 'C':
    print('Usted ha votado por el partido AZUL')
else:
    print('Opción errónea!')