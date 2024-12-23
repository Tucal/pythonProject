print(f'','='*50)
print(f'\n''              10 Termos de uma PA')
print(f'\n','='*50)

# Verificando o 1° termo e defininfo a razão
primeiro = int(input('\nPrimeiro Termo: '))
razao = int(input('Razão:'))
decimo = (primeiro+(10-1)*razao)

# Inicializando o loop
for i in range(primeiro,decimo + razao ,razao):
        print(f'{i}', end = " -> ")
print('Acabou')

