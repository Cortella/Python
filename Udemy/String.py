nome = "Bruno"
sobreNome = "Machado"
concatenar = nome + " " + sobreNome + "\n"
print(concatenar)
print(concatenar.__len__())
print(concatenar[3])
print(concatenar[2:5])
print(concatenar.lower())
print(concatenar.upper())
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r")
print(minha_lista)

busca = minha_string.find("rei")
print(busca)

minha_string = minha_string.replace("do rei","da rainha")
print(minha_string)
