from math import floor
from math import sqrt
from math import sin
from math import cos
from math import tan
import random

num = float(input("Digite um numero real"))
print("Parte inteira = {}".format(floor(num)))
cateto1 = float(input("digite o valor do primeiro cateto"))
cateto2 = float(input("digite o valor do primeiro cateto"))
print("HIPOTENUSA = ",sqrt(pow(cateto1,2) + pow(cateto2,2)))
angulo = float(input("Digite um angulo: "))
print("SENO = ",sin(angulo))
print("COSSENO = ",cos(angulo))
print("TANGENTE = ",tan(angulo))
aluno1 = str(input("Digite o nome do aluno:"))
aluno2 = str(input("Digite o nome do aluno:"))
aluno3 = str(input("Digite o nome do aluno:"))
aluno4 = str(input("Digite o nome do aluno:"))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print("ESCOLHIDO  =  {}".format(escolhido))
random.shuffle(lista)
print(lista)
