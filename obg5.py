print("Valor mínimo do saque: R$10,00.")
print("Valor máximo do saque: R$600,00")
saque = int(input("Valor do saque: R$"))

while(saque<10 or saque>600):
    print("Valor fora dos limites.")
    saque = int(input("Digite novamente: R$"))
    break

if(saque>=10) and (saque<=600):
    resto1 = saque % 100
resto2 = resto1 % 50
resto3 = resto2 % 10
resto4 = resto3 % 5

nota100, nota50, nota10, nota5, nota1 = saque//100,resto1//50,resto2//10,resto3//5,resto4//1
print("Notas de R$100,00:",nota100)
print("Notas de R$50,00:",nota50)
print("Notas de R$10,00:",nota10)
print("Notas de R$5,00:",nota5)
print("Notas de R$1,00:",nota1)
