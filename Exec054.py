from datetime import datetime
ano = datetime.now().year

# Lista para armazenar as idades
idades = []

# contadores para maiores e menores
maior = 0
menor = 0

# Executando loop para apresentar a idade de 7 pessoas
for a in range(1,8):
    dataNascimento = int(input('Informe o ano em que você nasceu: '))
    idade = (ano-dataNascimento) # Calculando a idade
    idades.append(idade) # Adicionar a idade na lista
    if idade >= 18:
        maior += 1
    else:
        menor += 1

# Exibindo o total de maiores e menores de idade
print(f'\nLista de idades:', idades)
print(f'\nMaiores de idade: {maior}')
print(f'\nMenores de idade: {menor}')





