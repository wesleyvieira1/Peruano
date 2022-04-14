#Declaro o nome da classe
class Complexo:

    #Definindo Acumuladoopcao_menu
    real = img = 0

    #Função Construtora
    def __init__(self, real, img):
        self.real = real
        self.img  = img

    #Função de soma
    def __add__(self, outro):
        preal = self.real + outro.real
        pimg  = self.img  + outro.img

        return Complexo(preal, pimg)
    
    #Função de subtração
    def __sub__(self, outro):
        preal = self.real - outro.real
        pimg  = self.img  - outro.img

        return Complexo(preal, pimg)
    
    #Função de multiplicação
    def __mul__(self, outro):
        preal = self.real*outro.real - self.img*outro.img
        pimg  = self.real*outro.img + self.img*outro.real

        return Complexo(preal, pimg)
    
    
    #Função de divisão real
    def __truediv__(self, outro):

        #Definindo Número conjurado
        Nconju = -(outro.img)
        
        #Distributiva do Numerador
        preal = self.real*outro.real + (self.img *-1*Nconju)
        pimg = self.real * Nconju + self.img*outro.real
        
        #Distributiva do Denominador
        mconju = outro.real*outro.real + (outro.img*Nconju*-1)
        
        return Complexo(preal,pimg), mconju


    #Menor que
    def __lt__(self,outro):
        q1 = ((self.real**2 + self.img**2)**(1/2))
        q2 = ((outro.real**2 + outro.img**2)**(1/2))

        return q1<q2

    #Menor ou igual que
    def __le__(self,outro):
        q1 = ((self.real**2 + self.img**2)**(1/2))
        q2 = ((outro.real**2 + outro.img**2)**(1/2))

        return q1<=q2

    #Igualdade
    def __eq__(self,outro):
        q1 = self.real
        q2 = self.img
        q3 = outro.real
        q4 = outro.img

        return (q1==q2 and q3==q4)

    #Diferente de
    def __ne__(self,outro):
        q1 = self.real
        q2 = self.img
        q3 = outro.real
        q4 = outro.img
        return (q1!=q2 and q3!=q4)

    #Maior que
    def __gt__(self,outro):
        q1 = ((self.real**2 + self.img**2)**(1/2))
        q2 = ((outro.real**2 + outro.img**2)**(1/2))

        return q1>q2

    #Maior ou igual que
    def __ge__(self,outro):
        q1 = ((self.real**2 + self.img**2)**(1/2))
        q2 = ((outro.real**2 + outro.img**2)**(1/2))

        return q1>=q2

    
    #Função de string - Criadora da saída
    def __str__(self):
        if(self.img<0):
            formato = str(self.real) + str(self.img)+"i"
        else:
            formato = str(self.real) + "+"+str(self.img)+"i"
        return formato


#Entrada de dados
def main():
    c1 = Complexo(6,5)
    c2 = Complexo(2,-1)
    

#Documentação da TAD
    print("")
    print(""" \033[1;31mEssa classe (TAD) calcula números complexos, segue o menu e 
            escolha a operação desejada:\033[0:0m """)
    print("")

    #Criando o menu de opções com cores
    print("\033[1;33m            ---------------------\033[0:0m")
    print("           \033[1;33m|\033[0:0m   \033[1;33m MENU DE OPÇÕES\033[0:0m  \033[1;33m |\033[0:0m ")
    print("\033[1;33m            ---------------------\033[0:0m")
    
    menu = '''
       | \033[1;33m[1]\033[0:0m Soma                   |
       | \033[1;33m[2]\033[0:0m Subtração              |
       | \033[1;33m[3]\033[0:0m Multiplicação          |
       | \033[1;33m[4]\033[0:0m Divisão                |
       | \033[1;33m[5]\033[0:0m Operações Relacionais  |
       | \033[1;33m[6]\033[0:0m Sair                   |
        
        '''
    print(menu)
    
    #Opção de escolha
    opcao_menu = int(input("Digite sua opção: "))
    
    #Condições de escolha
    if (opcao_menu==1):
        c3 = c1 + c2
        print("\n")
        print(str(c1)+" + "+ str(c2) + " = " + str(c3))
            
    if (opcao_menu==2):
        c4 = c1 - c2
        print("\n")
        print(str(c1)+" - "+ str(c2) + " = " + str(c4))

    if (opcao_menu==3):
        c5 = c1 * c2
        print("\n")
        print(str(c1)+" x "+ str(c2) + " = " + str(c5))

    if (opcao_menu==4):
        d1,d2 = c1/c2
        print("\n")
        print(str(c1)+" : "+ str(c2) + " = " + str(d1)+"/"+ str(d2))

    if (opcao_menu==5):
        print("\033[1;32m            ---------------------------\033[0:0m")
        print("           \033[1;32m|\033[0:0m   \033[1;32mOPERAÇÕES RELACIONAIS\033[0:0m  \033[1;32m |\033[0:0m ")
        print("\033[1;32m            ---------------------------\033[0:0m")
        
        #Criando a tabela de operações relacionais
        tabela = """
            \033[1;32m[A]\033[0:0m >  : Maior que
            \033[1;32m[B]\033[0:0m >= : Maior ou igual
            \033[1;32m[C]\033[0:0m <  : Menor que
            \033[1;32m[D]\033[0:0m <= : Menor ou igual
            \033[1;32m[E]\033[0:0m == : Igualdade
            \033[1;32m[F]\033[0:0m != : Diferente de
            \033[1;32m[S]\033[0:0m    : Sair

        """
        print(tabela)
        res = str(input("Digite sua opção: "))
        
        #Condições de escolha
        if res=="A":
            c5 = c1>c2
            print(c5)
        
        if res=="B":
            c5 = c1>=c2
            print(c5)

        if res=="C":
            c5 = c1<c2
            print(c5)
        
        if res=="D":
            c5 = c1<=c2
            print(c5)

        if res=="E":
            c5 = c1==c2
            print(c5)

        if res=="F":
            c5 = c1!=c2
            print(c5)
        
        if res=="S":
            exit("\nFechando Tabela...")
    
    if (opcao_menu==6):
        exit("\n Seu programa está fechando...")

#Chamada da função main()
if __name__=="__main__":
    main()