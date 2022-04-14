#        -==JOGO DA FORCA==-
#             Code by: 
#          ig: @wesleyhsv 

from time import sleep

def jogoDaForca(palavra):
    print("\n"*100)
    
    #Subsitui as letras da palavra por "-"
    for i in range(0,len(palavra)):
        descoberta.append('-')
    print("Seu game está sendo organizado...")
    sleep(1.20)
    print("Pronto.\n")

    #Mostra os dados que o jogador irá receber
    print("|{}|".format("="*22))
    print("""     -==DADOS==-

      Vidas: 6    
      Dica: {}           
      Tema: {}                  """.format(dica,tema))
    print("|{}|\n".format("="*22))

    print(f"Sua palavra tem {len(palavra)} letras.")
    print(descoberta)
    acertos = False

    #Total de vidas
    cont_digit = 6
    
    #Cria um loop até acertos ser True
    while acertos == False:
        newLettter = str(input("\nDigite uma letra: "))
        
        #Verifica se jogador digitou algo na variável palavra
        if newLettter == "":
            print("Você não digitou nada!")
            newLettter = str(input("Digite um letra: "))
        
        #A cada erro uma vida do jogador diminui
        if newLettter not in palavra:
            cont_digit-=1
            
            #Verifica se o jogador já usou todas as suas vidas
            if cont_digit == 0:
                exit("Você perdeu! Usou todas as suas vidas...!")
            digitada.append(newLettter)
            print(f"Não tem a letra {newLettter} \n")
            
            #Mostra as letras erradas que foram digitadas e o número de vidas do jogador
            if newLettter in digitada:
                
                print(f"A(s) letra(s) digitada(s): {digitada}")
                print(f"Lembre-se: Você ainda tem {cont_digit} vidas!\n")
    
        #percorre a palavra e verifica se a letra digitada pertence a palavra
        for i in range (0,len(palavra)):
            
            if newLettter in palavra[i]:
                descoberta[i] = newLettter
            print(descoberta[i])
        acertos = True
        #Após se ainda tiver "-" na descoberta o jogador ainda não encontrou todas as palavras
        for k in range(0,len(descoberta)):
            
            if "-" in descoberta[k]:
                acertos = False
    #Verifica se a palavra está completa e se o jogador ainda tem vidas
    if "-" not in descoberta and cont_digit>0:
        print("\n\033[1;31mPARABÉNS VOCÊ ACERTOU!!\033[1;31m")
        return (f"\nA palavra é {palavra}.\n")
    else:
        return exit()
        




digitada = []
descoberta = []

print("|{}|".format("="*41))
print("|              JOGO DA FORCA              |")
print("|{}|\n".format("="*41))

palavra = str(input("Digite uma palavra para iniciar o game: ")).lower().strip()
tema = str(input("Digite uma tema relacionado a palavra: "))
dica = str(input("Digite uma dica relacionada a palavra: "))

print(jogoDaForca(palavra))