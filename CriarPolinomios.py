def CriarPolinomios(*nums):
    """
        Essa rotina cria polinômios de qualquer grau.
    """

    #Definindo Acumuladores
    acc = 0
    text = " "
    grau = len(nums) - 1

    #Criando a saída
    for i in nums:
        if acc - grau != 0:
            if i>0:
                text+="+" + str(i) + "x" + str(grau - acc)
            elif i<0:
                text+=" " + str(i) + "x" + str(grau - acc)
        else:
            if i>0:
                text+="+" + str(i)
            elif i<0:
                text+=" " + str(i)
        acc+=1
    print("")

    #Verificação de sinal negativo
    formata = text.find("-")
    if "-" in text:
        newText = text[:formata-1]+text[formata:]
        return newText
    else:
        return text

#Documentação da rotina
print("A documentação da rotina é:")
print(CriarPolinomios.__doc__)

#Entrada e Saída de Dados
print(CriarPolinomios(2,1))
print(CriarPolinomios(4,0,2))
print(CriarPolinomios(2,-3,1))
print(CriarPolinomios(6,2,-3,1))