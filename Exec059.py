#  Recebendo valores inteiros
print('------ Inicio ------')
n1 = int(input('\nDigite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
new_number = 0

def somar():
    print("Função Somar")

def multiplicar():
    print("Função Multiplicar")

def maior():
    print("Função Maior")

def novos_numeros():
    print("Novos números")

def sair():
    print("Saindo do programa")
    exit()

menu = {
    1: somar,
    2: multiplicar,
    3: maior,
    4: novos_numeros,
    5: sair
}

def exibir_menu():
    print("\nEscolha uma opção:")
    while True:
        for chave in menu:
            print(f"{chave} - {menu[chave].__name__.capitalize()}")
        try:
            opcao = int(input("\nOpção: "))
            if opcao in menu:
                menu[opcao]()  # Executa a função correspondente à opção escolhida
                if opcao==1:
                    soma=(n1+n2)
                    print(f'\nResultado: {soma}')
                    break
                elif opcao==5:
                    break  # Sai do loop se a opção for "sair"
                elif opcao==2:
                    multiplicar = (n1*n2)
                    print(f'\nResultado: {multiplicar}')
                    break
                elif opcao==3:
                     if  n1 > n2:
                         print(f'\nO número {n1} é maior.')
                     elif n1 == n2:
                         print("Os números informados são iguais.")
                     else:
                         print(f'\nO número {n2} é maior.')
                     break
                else:
                    print(f'')
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Exemplo de uso
exibir_menu()
