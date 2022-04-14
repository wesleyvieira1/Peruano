def PrimoRecursivo(num,div=2):
    if num==1:
        return num
    else:
        if div<=num/2:
            if num%div!=0:
                return PrimoRecursivo(num,div+1)
                
            else:
                return False
        else:
            return True
num = int(input("Digite um número: "))
print(PrimoRecursivo(num))