'''Ejercicio 1
En la siguiente lista, debes hacer un programa que muestre los
valores al usuario, a su vez, debe pedir dos datos y esos que sean
ingresados deben ser sustituidos en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]'''
lista = [20, 50, "Curso", 'Python', 3.14]
print('Lista original: ', lista)

a = input('Ahora ingresa un dato: ')
b = input('Ingresa otro dato: ')

lista[0] = a
lista[1] = b

print('Ahora la lista es la siguiente: ', lista)

'''Ejercicio 2
Escribe una lista que tenga los números de 1 al 10. Luego, debes
hacer que los datos que están en las posiciones 4, 7 y 9 sean
multiplicados por 2; por último, mostrar la lista nueva con los
nuevos datos'''
lista2 = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
print('Lista original: ', lista2)

lista2[3] = lista2[3] * 2
lista2[6] = lista2[6] * 2
lista2[8] *= 2

print('Lista final: ', lista2)