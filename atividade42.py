# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica. Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos de 45%, prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao consumidor.

CF = int(input('Qual o custo da fábrica do carro? '))
Dis = CF * 0.12
I = CF * 0.45
V = CF+Dis+I
print("O valor final do carro é:", V)