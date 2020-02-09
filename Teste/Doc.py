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
#EXEMPLO DO USO DE INPUTS
#INPUT E CASTING PARA INT AUTOMATICO
#SISTEMA DE CALCULOS

x = int(input("digite um valor"))
y = int(input("digite um valor"))

print("SOMA =",x+y)