#Uma empresa de piscinas precisa saber qual o volume em que cada piscina terá em M³, sendo que o usuário irá informar a largura, comprimento e profundidade.


largura= float(input('Informe a largura:'))
comprimento= float(input('Informe o comprimento:'))
profundidade= float(input('Informe a profundidade:'))
formula= largura*comprimento*profundidade
print(f' O volume da piscina será de : {formula}')