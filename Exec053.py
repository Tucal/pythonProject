# Entrada de Dados sendo tratada para remover os espaços
frase = str(input('Digite uma frase: ')).replace(" ", "").lower().strip()
#Invertendo a entrada de informações
invertendo = frase[::-1]
# Removendo todos os espaços em branco
if (frase == invertendo):
    print(f"\n\033[0;31m O inverso de {frase} é '{invertendo}'. Então é palíndromo !\033[m")
else:
    print('\nÉ uma frase comum !')
