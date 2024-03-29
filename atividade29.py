#Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 11% de previdência social, e após isso 8% para imposto de renda.

diastrabalhados = int(input("Digite o número de dias trabalhados: "))
salariobruto = diastrabalhados * 30
descontoprevidencia = salariobruto * 0.11
descontoimpostorenda = salariobruto * 0.08
salarioliquido = salariobruto - descontoprevidencia - descontoimpostorenda

print(f' O salário a ser pago deve ser de {salarioliquido}')