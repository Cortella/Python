nome = str(input("digite seu nome")).strip()
print(nome.upper())
print(nome.lower())
print("Seu nome todo tem {}".format(len(nome)-nome.count(' ')))
novoNome = nome.split()
print("Seu primeiro nome = {} e tem {} letras".format(novoNome[0],len(novoNome[0])))
