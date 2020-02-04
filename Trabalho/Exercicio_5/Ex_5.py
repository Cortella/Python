n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))

if (n1<n2) and (n1<n3):
    print(n1, "é o menor dos numeros")
elif(n2<n3):
    print(n2, "é o menor dos numeros")
else:
    print(n3, "é o menor dos numeros")
