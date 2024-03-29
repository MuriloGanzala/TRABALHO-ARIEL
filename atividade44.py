#Uma companhia de carros paga a seus empregados um salário de R$ 500,00 por mês mais uma comissão de R$ 50,00 para cada carro vendido e mais 5% do valor da venda. Elabore um algoritmo para calcular e imprimir o salário do vendedor num dado mês recebendo como dados de entrada o nome do vendedor, o número de carros vendidos e o valor total das vendas.

nomedovendedor= (input('Solicite o nome do vendedor'))
numerodecarrosvendidos = int(input('Solicite o número de carros vendidos'))
valortotaldevendas= int(input('Solicite o valor total de vendas'))
calculo= numerodecarrosvendidos*50.00
comissao=calculo* 0.5
salario= calculo+comissao+500
print(f'{nomedovendedor} , o seu salário é' , salario)

