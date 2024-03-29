#Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: 𝑅 = 𝐺 ∗ 𝜋/180, sendo 𝐺 o ângulo em graus e 𝑅 em radianos e 𝜋 = 3.14

angulo= float(input('Digite quantos graus esta o angulo:'))
formula= angulo*3.14/180
print(f' A transformação em radiano fica de {formula}')