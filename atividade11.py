#Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). A fórmula de conversão é: 𝐾 = 𝑀 ∗ 3.6, sendo 𝐾 a velocidade em km/h e 𝑀 em m/s.

velocidade= float(input('Digite a velocidade em m/s:'))
formula= velocidade*3.6
print(f'A velocidade é de {formula} em km/h')