# Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário em uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.

salariobase = float(input("Digite o salário-base do funcionário: "))

gratificacao = salariobase * 0.05
imposto = salariobase * 0.07

salarioreceber = salariobase + gratificacao - imposto

print(f'O salário a receber é de: {salarioreceber}')