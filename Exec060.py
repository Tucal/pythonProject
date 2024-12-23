#Informando um número
number = int(input('Informe um número:'))

# Fatorial
fatorial = 1
contador = number

if number <  0:
    print("Não existe fatorial para números negativos.")
elif number == 0:
    print('Fatorial de 0 é 1')
else:
    while contador > 0:
        fatorial*=contador
        contador-=1
    print(f'\nO fatoria de {number} é {fatorial}.')


