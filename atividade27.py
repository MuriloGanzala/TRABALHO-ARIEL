#Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um monstruoso aumento de 1.77%. 

salario= float(input('Digite o seu salário:'))
novosalario= 1.77/salario
contanovo= salario+novosalario
print(f'O seu novo salário é de: {contanovo}')