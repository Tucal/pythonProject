# Variáveis
mulher20 = 0
soma = 0
velho = 0
nomevelho = ""

for i in range(1,5):
        print(f'--- Dados das pessoas {i}ª ---')
        name = str(input("Nome:")).strip()
        idade = int(input('Idade:'))
        sexo = str(input('Sexo [M/F]:')).strip().upper()

        #Soma das idades para cálculo da média
        soma += idade

        # Verifica o homem mais velho
        if sexo == 'M' and idade > velho:
            velho = idade
            nomevelho = name

        # Conta mulheres com menos de 20 anos
        if sexo == 'F' and idade < 20:
            mulher20 += 1

# Extraido a média de idade das pessoas
average = (soma/i)

# Exibindo resultados
print("\n--- Resultados ---")
print(f'\nA média de idades destas pessoas é de {average:.0f} anos')
if velho:
    print(f'\nO homem mais velho é {nomevelho}, com idade {velho} anos.')
else:
    print('Não há homens neste grupo')
print(f"\nHá {mulher20} mulher(es) com menos de 20 anos.")