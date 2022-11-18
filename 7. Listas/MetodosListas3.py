lista = ['Python', 24, 'Daniel', 'rosas', 13]

lista[3] = 'Rosas' #Para modificar un datos especifico
print(lista)

'''Para eliminar datos que no nos sirvan'''
lista.pop() #Toma el último dato y lo elimina
print(lista)
lista.pop()
print(lista)

lista.remove('Python') #Borra directamente lo que le indico
print(lista)