'''Ejercicio 1
Realiza un programa que haga el proceso de formula general
para la resolución de ecuaciones, sabiendo que la formula
general es la que está en la imagen, el usuario debe ingresar los
valores de a, b y c, y el programa debe hacer el proceso para
que al final muestre el mensaje: La solución es: <Solución>'''
from cmath import sqrt #Si pongo math, en raices negativas me arroja error


print('Formula general\n')
a = float(input('Ingresa el valor de "a": '))
b = float(input('Ingresa el valor de "b": '))
c = float(input('Ingresa el valor de "c": '))
x1 = ((-b)+(sqrt((b*b)-(4*a*c))))/(2*a)
x2 = ((-b)-(sqrt((b*b)-(4*a*c))))/(2*a)

print('La solución es: x1=', x1, 'x2=', x2)

'''Ejercicio 2
Se desea tener un algoritmo que permita determinar y mostrar el
promedio que ha obtenido un alumno en un determinado curso,
conociendo las notas de: tres prácticas, el examen parcial y el
examen final
Considere:
PP = (P1+P2+P3)/3 PROM = (PP+2*EP+3*EF)/6
Donde: 
P1, P2, P3: Practicas
PP: Promedio de práctica
PROM: Promedio
EP: Examen parcial
EF: Examen final'''
alumno = input('Ingrese nombre del alumno: ')
p1 = float(input('Ingrese calificación de practica 1: '))
p2 = float(input('Ingrese calificación de practica 2: '))
p3 = float(input('Ingrese calificación de practica 3: '))
ep = float(input('Ingrese calificación del examen parcial: '))
ef = float(input('Ingrese calificación del examen final: '))

pp = (p1+p2+p3)/(3)
prom = ((pp)+(2*ep)+(3*ef))/(6)

print('Promedio final del alumno: ', alumno, 'es:', prom)