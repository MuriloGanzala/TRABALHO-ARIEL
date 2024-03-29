#Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

altura= float(input('Digite a altura do degrau da escada:'))
deseja= float(input('Digite qual a altura voce deseja alcançar com a escada:'))
conta= deseja/altura

print(f'Você tera que subir {conta} degraus.')