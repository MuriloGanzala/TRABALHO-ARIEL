#Calcule a média de um aluno na disciplina de ED. Para isso solicite o nome do aluno, a nota da prova e a nota qualitativa. Sabe-se que a nota da prova tem peso 2 e a nota qualitativa peso 1. Mostre a média como resultado

nomedoaluno= (input('Informe o seu nome:'))

notadaprova= int(input('Informe a nota da prova:'))

notaqualitativa= int(input('Informe a nota qualitativa:'))

media= (notaqualitativa+(notadaprova*2)/3)

print(f'{nomedoaluno} a sua média final é {media}')