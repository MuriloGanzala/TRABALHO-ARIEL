#Sejam 𝑏 e 𝑏 os catetos de um triangulo, onde a hipotenusa é obtida pela equação ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √𝑎 2 + 𝑏². Faça um programa que receba os valores de 𝑎 e 𝑏 e calculo o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

a= float(input('Digite o valor de A:'))
b= float(input('Digite o valor de B:'))

conta= (a*a+b*b)**0.5

print(f'O valor da hipotenusa é: {conta}')