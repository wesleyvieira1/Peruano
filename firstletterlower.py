nome = str(input("Digite seu nome completo: "))

separar = nome.split()
lista = []
for palavra in separar:
    a = palavra.title()
    lista.append(a)

print(' '.join(lista))