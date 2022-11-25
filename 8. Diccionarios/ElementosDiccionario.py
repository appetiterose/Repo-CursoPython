diccionario = {'Nombre' : 'Daniel', 'Apellido' : 'Rosas', 'Estatura' : 1.79}

print(diccionario)
print(diccionario.keys())
print(diccionario.values())

print(diccionario['Estatura']) #Mandar a llamar un valor

diccionario['Peso'] = '58 Kg' #Agregar nuevo valor
print(diccionario)

diccionario['Nombre'] = 'daniel' #Modificar un valor
print(diccionario)