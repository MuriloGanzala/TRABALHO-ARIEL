#Sabendo que a formula para aprovação é: 𝐺1+(𝐺2∗2)3≥ 7.0, desenvolva uma aplicação que leia as notas de G1 e G2 e apresente a média do semestre.

g1= int(input('Digite a nota 1:'))
g2= int(input('Digite a nota 2:'))

media= g1+(g2*2)/3 
print(f'A sua media é de: {media}')