# Inicializa a soma dos números pares
soma_pares = 0
cont = 0

# Loop para leitura de seis números inteiros
print("\nDigite 6 números inteiros")
for i in range(6):
    numero = int(input(f"\nNúmero {i + 1}: "))

    # Verifica se o número é par
    if numero % 2 == 0:
        soma_pares += numero
        cont += 1

# Exibe a soma dos números pares
print(f"A soma dos números pares digitados é: {soma_pares}")
print(f'Quantidade de números pares: {cont}')
