def tiaJuice(arq):
    """
    Essa função codifica nome de arquivos pelo método de 
             criptografiada da tia juice.
    """
    arqCript = []
    dic = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
    }
    
    arqSemExt = ((((arq[:-1])[:-1])[:-1])[:-1]) #gabi
    cont = len(arqSemExt) # 4
    

    for i in arqSemExt: # g=7+4 a=1+4 b=2+4 i=9+4
        arqCript.append(str(int(dic.get(i))+int(cont))) #[11,5,6,13]
    
    ext = "_".join(arqCript) #11_5_6_13
    return ext + ".juice" #11_5_6_13.juice

def main():
    print("A documentação da rotina é:")
    print(tiaJuice.__doc__)
    
    arq = str(input("Digite o nome do Arquivo: ")) #gabi.txt
    print("Arquivo Criptografado:",tiaJuice(arq))
if __name__=="__main__":
    main()