#Faça um programa que leia o valor da hora de trabalho em reais e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

valorhora= float(input('Digite o valor da sua hora:'))
horastrabalhadas= float(input('Digite a quantidade de horas trabalhadas:'))

conta= (valorhora*horastrabalhadas)
conta2= conta*0.10
conta3= conta+conta2

print(f'O seu salário é de: {conta3}')