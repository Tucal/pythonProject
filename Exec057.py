import emoji
while True:
    sexo = str(input('\nInforme o seu  sexo:')).lower().strip()
    if (sexo == 'm'):
        print('\n\033[0;34mSexo masculino\033[0m')
        break # Encerra loop
    elif (sexo == 'f'):
        print(f'\n\033[0;31mSexo Feminino {emoji.emojize(":red_heart:")}\033[0m')
        break # Encerra loop
    else:
        print('\n\033[0;33mDados inválidos, por favor  informe o seu  sexo(M ou F).\033[0m')
print('\nFim')




