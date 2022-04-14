def AutoReverse(cadeia):
    cont = len(cadeia)
    if cont==1:
        return cadeia
    else:
        return cadeia[cont-1] + AutoReverse(cadeia[0:cont-1])
cadeia = str(input())
print(AutoReverse(cadeia))