# O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade de cada item que você consumiu e calcule a conta final. a. Hambúrguer................. R$ 3,00 b. Cheeseburger.............. R$ 2,50 c. Fritas............................ R$ 2,50 d. Refrigerante ................. R$ 1,00 e. Milkshake..................... R$ 3,00


hamburguer= int(input(' Qual a quantidade de hamburguer:'))
cheeseburguer= int(input('Qual é a quantidade de cheeseburguer:'))
fritas= int(input('Qual é a quantidade de fritas:'))
refrigerante = int(input('Qual é a quantidade de refrigerante:'))
milkshake= int (input('Qual é a quantidade de milkshake:'))
somatotal= (hamburguer*3.00) + (cheeseburguer*2.50) + (fritas*2.50) + (refrigerante*1.00) + (milkshake*3.00)
print(f' o valor total da conta é', somatotal )

