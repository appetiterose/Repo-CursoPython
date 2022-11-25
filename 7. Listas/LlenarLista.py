lista = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = lista + lista2
print(lista3)

#print("Esta es una lista de distinto datos: "+ lista3)#No se puede
print("Esta es una lista de distinto datos: ", lista3)# Si se puede

lista4 = []
edad = int(input('Ingresa tu edad: '))
lista4.append(edad)

print(lista4)