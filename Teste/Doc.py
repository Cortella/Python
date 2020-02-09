# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 03:02:56 2020

@author: cortella
"""

#USO DE CONDICIONAIS 

idade = int(input("Digite sua idade"))

if idade >= 18:
    print("voce ja pode dirigir")
if idade < 18:
    print("voce nao pode dirigir")
    
#USO DO ELSE
if idade >= 18:
    print("voce ja pode dirigir")
else:
    print("voce nao pode dirigir")
    

#IF COMPOSTO
    if idade >=20:
        if idade <=60:
            print("IDADE ENTRE 20 E 60 ANOS")
        else:
            print("IDADE FORA DO PADRAO")
    else:
        print("IDADE FORA DO PADRAO")
#IFS DEPENDENTES
numero = 2
if(numero == 1):
    print("Segunda")
if(numero == 2):
    print("Terca")
if(numero == 3):
    print("Quarta")
if(numero == 4):
    print("Quinta")
if(numero == 5):
    print("Sexta")
if(numero == 6):
    print("Sabado")
if(numero == 7):
    print("Domingo")
else:
    print("Numero invalido")
    
#IFS INDEPENDENTES (DEPENDENTES APENAS DO PRIMEIRO IF)
if(numero == 1):
    print("Segunda")
elif(numero == 2):
    print("Terca")
elif(numero == 3):
    print("Quarta")
elif(numero == 4):
    print("Quinta")
elif(numero == 5):
    print("Sexta")
elif(numero == 6):
    print("Sabado")
elif(numero == 7):
    print("Domingo")
else:
    print("Numero invalido")
#EXEMPLO DO USO DE INPUTS
#INPUT E CASTING PARA INT AUTOMATICO
#SISTEMA DE CALCULOS

x = int(input("digite um valor"))
y = int(input("digite um valor"))

print("SOMA =",x+y)

#LACO DE REPETICAO

n = 10
cont = 0
#WHILE
while cont < n :
    print(cont)
    cont++