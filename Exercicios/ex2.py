import random


num = int(input("Digite um valor real inteiro aleatório: "))

vetor = []
for i in range(num):
    vetor.append(random.randint(1,1000))

print (vetor)