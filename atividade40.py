#Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido

a1= float(input(' valor investido pelo primeiro amigo:'))
a2= float(input(' valor investido pelo segundo amigo:'))

a3= float(input(' valor investido pelo terceiro amigo:'))
soma=a1+a2+a3

vlrpremio= float(input('Digite o valor do premio:'))
print(f'O jogador A receberá {(a1/soma)*vlrpremio}')
print(f'O jogador B receberá {(a2/soma)*vlrpremio}')
print(f'O jogador C receberá {(a3/soma)*vlrpremio}')

