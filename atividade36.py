


# Solicita o número inteiro positivo de três dígitos

numero = int(input("Digite um número inteiro positivo de três dígitos (de 100 a 999): "))
    
# Verifica se o número possui três dígitos
if 100 <= numero <= 999:
# Inverte os dígitos do número
    numero_invertido = int(str(numero)[::-1])
# Exibe o número invertido
    print("O número com os dígitos invertidos é:", numero_invertido)

else:
     print("O número digitado não está no intervalo de 100 a 999.")

