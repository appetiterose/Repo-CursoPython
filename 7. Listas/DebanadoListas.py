lista = [10, 20, 3.14, 'Daniel', 'Rosas', 7, 'Empleado', 'cuaderno']

print(lista[5])
print(lista[0 : 5]) #El 5 no se imprime, es el limite
print(lista[ : 2])
print(lista[1 : ]) #En este caso si imprime desde el 1
print(lista[-1])
print(lista[-2 : 2]) # Esto no se puede
print(lista[-5 : -2]) #El valor mayor va a la izquierda