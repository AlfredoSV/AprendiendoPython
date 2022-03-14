# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:24:42 2022

@author: Alfredo
"""

nombres = ["Alfredo","Jorge","Ana"]

#Acceder a item por indice

print(nombres[1])

print("-----------------------------")

#Recorrer lista

i = 0

for nombre in nombres:
    print(i,":",nombre)
    i+=1

print("------------------------")

#Concatenar listas

nombres2 = ["Sofia","Alenjandra","Axel"]

i = 0
while i < len(nombres2):
    nombres.append((nombres2[i]))
    i+=1

print(nombres)    
    
#Slices

listaNumeros = list(range(1,20))

print(listaNumeros[1:5])

print(listaNumeros[0:10:2])



#Recorrer más de una lista

for nombre1,nombre2 in zip(nombres,nombres2):
    print("Nombre1: " + nombre1, "Nombre2: " + nombre2)



#Operadores de pertenencia

print(200 not in listaNumeros)

print(5 in listaNumeros)



