numeric = int(input('Digite um número: '))

if numeric > 1:
    # Verifica divisores no intervalo de 2 até a raiz quadrada do número
    for i in range(2,int(numeric**0.5) + 1):
        if numeric % i == 0:
            print(f"{numeric} não é primo. Divisível por {i}.")
            break
    else:
        print(f'{numeric} é um número primo')
else:
    print(f'{numeric} não é primo, pois deve ser maior que 1.')