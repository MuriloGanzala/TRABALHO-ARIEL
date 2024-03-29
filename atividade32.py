#Escreva um programa de ajuda para vendedor. A partir de um valor total lido mostre: a. O total a pagar com desconto de 10%; b. O valor de cada parcela, no parcelamento de 3x sem juros; c. A comissão do vendedor, caso de a venda ser a vista (5% sobre o valor com desconto); d. A comissão do vendedor, caso de a venda ser parcelada (5% sobre o valor  total)


valor=float(input('Digite o valor do produto:'))
desconto= valor*0.10
novovalor= valor-desconto
print(f'O valor do produto com desconto é de: {novovalor}')
            
valordeparcela= novovalor/3
print(f'O valor de cada parcela em 3 vezes sem juros é de: {valordeparcela}')  

comissao= novovalor*0.05
print(f'A comissão do vendedor caso a venda seja a vista será de:{comissao}')          

comissao2= valor*0.05
print(f' A comissão do vendedor caso a venda seja feita parcelada será de: {comissao2}')