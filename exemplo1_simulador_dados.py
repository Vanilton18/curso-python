import random
import statistics

quantidade = int(input("Digite a quantidade: "))
numeros = []
soma = 0
for i in range(quantidade):
    numero = random.randint(1, 6)
    numeros.append(numero)
    soma += numero
    print("Número gerado", numero)
print("Soma: ", sum(numeros))
print("Máximo: ", max(numeros))
print("Média: ", statistics.mean(numeros))
print("Desvio Padrao: ", statistics.stdev(numeros))