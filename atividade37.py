#Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos


segundos_total = int(input("Digite um valor inteiro em segundos: "))

horas = segundos_total // 3600
minutos = (segundos_total % 3600) // 60
segundos = segundos_total % 60
    
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)

