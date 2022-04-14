def bubbleSort(vetor):
    
    change = True
    i = 0

    while (change and i<len(vetor)):
        change = False
        
        for j in range (len(vetor)-1,i,-1):
            if vetor[j]<vetor[j-1]:
                aux = vetor[j-1]
                vetor[j-1] = vetor[j]
                vetor[j] = aux
                change = True
                print(vetor)

        i+=1
    return vetor

vetor = [5,4,3,2,1]
print(bubbleSort(vetor))