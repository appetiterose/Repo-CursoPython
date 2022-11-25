diccionario = {1 : 2, 2 : 3, 3 : 4}
diccionario2 = {4 : 5, 6 : 7}

print(diccionario)
diccionario.pop(3) #Aqui es diferente el pop, indicamos la llave
print(diccionario) #Tanto valor como llave se eliminan

'''diccionario.clear() #Borra como tal el diccionario
print(diccionario)'''

print(diccionario.get(2)) #Metodo para mostrar llave 2

diccionario.setdefault(4 , 10) #Agregamos al diccionario
print(diccionario)

diccionario.update(diccionario2) # Actualizamos diccionario y creamos uno solo
print(diccionario)

diccionario.copy() #Generamos una copia del diccionario
print(diccionario)