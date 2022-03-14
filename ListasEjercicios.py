# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:52:08 2022

@author: Alfredo
"""
import random
import math

"""Ejercicio 1Permalink
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
"""
"""

listaAleatoria = []

for i in range(1, 11):
    listaAleatoria += [random.randrange(1, 10)]


print(listaAleatoria)

for i in listaAleatoria:
    print(i,int(math.pow(i, 2)),int(math.pow(i, 3)))
"""


"""Ejercicio 2Permalink
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
"""
"""
listaCaracteres = []
listaCaracteres2 = []

for i in range(1,6):
    listaCaracteres += [input("Cadena " + str(i) + ":")]

listaCaracteres2 = listaCaracteres.copy()
listaCaracteres2.reverse()

print(listaCaracteres)

print(listaCaracteres2)
"""
"""Ejercicio 3Permalink
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
(comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media,
la nota más alta que ha sacado y la menor.
"""
"""
listaNotas = []


for i in range(1,6):
    nota = 0
    while True:
        nota = int(input("Nota " + str(i) + ":"))
        if(not(nota < 0 or nota > 10)):
            break;
        print("La nota " + str(nota) + " no se encuentra dentro del rango de 0 a 10")
        
    listaNotas += [nota]
    
print("Nota media:", int(sum(listaNotas)/len(listaNotas)))
print("Nota menor:", min(listaNotas))
print("Nota mayor:", max(listaNotas))

"""

"""Ejercicio 4Permalink
Programa que declare una lista y la vaya llenando de números 
hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector
(sólo los elementos introducidos).
"""
"""
listaNumerosPositivos = []

while True:
    numero = int(input("Num:"))
    if(numero < 0):
        break
    listaNumerosPositivos += [numero]
    
    
print(listaNumerosPositivos)
    
"""


"""Ejercicio 5Permalink
Hacer un programa que inicialice una lista de números con valores aleatorios
(10 valores), y posterior ordene los elementos de menor a mayor.
"""

"""
listaAleatoria5 = []

for i in range(1, 11):
    listaAleatoria5 += [random.randrange(1, 10)]

listaAleatoria5.sort();

print(listaAleatoria5)
"""

"""Ejercicio 6Permalink
Crea un programa que pida un número al usuario un número de mes
(por ejemplo, el 4) y diga cuántos días tiene
(por ejemplo, 30) y el nombre del mes. Debes usar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días.
"""
"""
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Ovtubre","Noviembre","Diciembre"]
diasPorMes = [30,28,30,30,30,30,30,30,30,30,30,30]

mes = int(input("Ingrese el número del mes:"))

print(meses[mes-1] + " tiene " + str(diasPorMes[mes-1]) + " días")

"""

"""Ejercicio 7Permalink
Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’
de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
"""
"""
lista1 = [1,2,3,4,6]
lista2 = [6,7,8,9,10]
lista3=[]
lista3 = lista1+lista2
print(lista3)
"""

"""Ejercicio 8Permalink
Queremos guardar los nombres y la edades de los alumnos de un curso.
Realiza un programa que introduzca el nombre y la edad de cada alumno.
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*)
Al finalizar se mostrará los siguientes datos:

Todos lo alumnos mayores de edad.
"""
"""
listaNombres = []
listaEdades = []
i = 1
resSeguir = ""

while True:
    listaNombres += [input("Ingrese el nombre del alumno " + str(i)+ " :") ]
    listaEdades += [int(input("Ingrese la edad del alumno " + str(i)+ " :"))]
    resSeguir = input("¿Desea realizar otra lectura?:")
    if resSeguir == "*":
        break
    i+=1
    
print(listaNombres)
print(listaEdades)
for nombre, edad in zip(listaNombres,listaEdades):
    if edad >= 18:
        print(nombre, edad)
    

"""

"""Ejercicio 9Permalink
Queremos guardar la temperatura mínima y máxima de 5 días. 
Realiza un programa que de la siguiente información:

*La temperatura media de cada día
*Se lee una temperatura por teclado y se muestran los días cuya 
temperatura máxima coincide con ella. si no existe ningún día se 
muestra un mensaje de información.
"""
"""

temperaturas = []

for i in range(1,3):
    dia = input("Día:")
    temMax = float(input("Temp max " + dia + ":"))
    temMin = float(input("Temp min " + dia + ":"))
    temperaturas += [(dia+";"+str(temMax)+";"+str(temMin))]
    
    
print("---Temp media---")
for tem in temperaturas:
    aux = tem.split(";")
    print(aux[0] +":" + str((float(aux[1])+float(aux[2])) / 2))

print("---Coincidencia Temp---")
tempBus = float(input("Temperarura a buscar:"))
existe = False
for tem in temperaturas:
    aux = tem.split(";")
    if(float(aux[1]) == tempBus):
       print(aux[0])   
       existe = True

if(not(existe)):
    print("No existe ninguna temp que haga match")       
      
"""



"""
Ejercicio 10Permalink
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
Carga la tabla con valores numéricos enteros.
Suma todos los elementos de cada fila y todos los elementos de cada columna 
visualizando los resultados en pantalla.
"""
tabla = []
tablaaux = []
tablaResFila = []
tablaResColumna = []
sumaFila = 0

for i in range(0,2):  
    tablaaux.clear()
    sumaFila = 0
    for j in range(0,5):
        tablaaux += [int(input("Valor (" + str(i) + "," + str(j) + ") :" ))]
        sumaFila += tablaaux[j]
    tablaResFila += [sumaFila]
    tabla += [tablaaux.copy()]

for i in range(0,2): 
    for j in range(0,5):
        if(len(tablaResColumna) < 5):
            tablaResColumna += [tabla[i][j]]
        else:
            tablaResColumna[j] += tabla[i][j]
            

    
print(tabla)
print(tablaResFila)
print(tablaResColumna)


"""Ejercicio 11Permalink
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
Muestra el contenido de la tabla en pantalla.

"""

"""Ejercicio 12Permalink
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.

  111111111111111
  100000000000001
  100000000000001
  100000000000001
  111111111111111
Visualiza el contenido de la matriz en pantalla.

"""

"""Ejercicio 13Permalink
De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.

Para guardar esta información se van a utilizar dos arreglos:

Nombre: Lista para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.

Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.
"""

"""Ejercicio 14Permalink
Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:

Las cantidades totales de cada articulo.
La cantidad de artículos en la sucursal 2.
La cantidad del articulo 3 en la sucursal 1.
La recaudación total de cada sucursal.
La recaudación total de la empresa.
La sucursal de mayor recaudación.
Ejercicio 15Permalink
Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:

Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?
"""
"""Ejercicio 16Permalink
Vamos a crear un programa que tenga el siguiente menú:

Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
Longitud de la lista: te muestra el número de elementos de la lista.
Eliminar el último número: Muestra el último número de la lista y lo borra.
Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
Mostrar números: Muestra los números de la lista
Salir

"""
"""Ejercicio 17Permalink
Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
"""
"""Ejercicio 18Permalink
Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
Eliminar: Me pide una cadena, y la elimina de la lista.
Mostrar: Muestra la lista de cadenas
Terminar
"""