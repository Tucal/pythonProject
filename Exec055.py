# Listando os pesos
list = []

for a in range(1,6):
        peso = float(input('Informe o seu peso atual:'))
        list.append(peso)

# Determinado o Maior e Menor Peso
maior = max(list)
menor = min(list)

# Exibindo valores
print(f'\nPesos:',list)
print(f'\nO Maior peso é o {maior} KG')
print(f'\nO Menor Peso é o {menor} KG')

