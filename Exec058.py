import random

print('-- Jogo de Adivinhação --')
print('\n-- Escolha um número de 1 a 10 --')
qtdTentativas = 0

while True:
    try:
        n = int(input('\nDigite a sua escolha:'))
        #  Validação de   Intervalo
        if  n < 1  or  n  > 10:
            print('\nEscolha uma opção válida entre 0 e 10.')
        c = random.randint(1,10)
        if n != c:
            qtdTentativas+=1
            print(f'\n\033[0;33mO número sorteado foi "{c}".\033[0m')
            print('\033[0;31mNão foi dessa vez, tente novammente.\033[0m')
        else:
            print(f'\n\033[0;33mO número sorteado foi "{c}".\033[0m')
            print('\n\033[0;34mParabéns!,você ganhou.\033[0m')
            print(f'\nForam {qtdTentativas} tentativa(s) até o senhor(a) ganhar.')
            break
    except ValueError:
        print('\033[0;31mPor favor, digite apenas números inteiros.\033[0m')
print('\nFim')


