n1 = int(input("Digite o primeiro numero:"))
n2 = int(input("Digite o segundo numero:"))
n3 = int(input("Digite o terceiro numero:"))

if (n1<n2) and (n1<n3) and (n1%2 == 1):
    print(n1, "é o menor impar dos numeros")
if (n2<n3) and (n2<n3) and (n2%2 == 1):
    print(n2, "é o menor impar dos numeros")
if (n3<n1) and (n3<n2) and (n3%2 == 1):
    print(n3, "é o menor impar dos numeros")
