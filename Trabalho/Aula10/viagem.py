distancia = float(input("digite a distancia em km"))
if distancia<=200.0:
    print("Preço da sua viagem = {} Reais".format(distancia*0.5))
else:
    print("Preço da sua viagem = {} Reais".format(distancia*0.45))
