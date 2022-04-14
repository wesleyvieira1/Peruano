def palindromo(texto):
    if texto == "" or len(texto) == 1:
        return True
    else:
        return texto[0] == texto[len(texto)-1]
texto = input("Digite uma palavra: ")
print(palindromo(texto))