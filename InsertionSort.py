def insertionSort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i
        while(j>0 and vetor[j-1]>chave):
            vetor[j] = vetor[j-1]
            j -= 1
            print(vetor)
        vetor[j] = chave
    return vetor

vetor = [5, 3, 4, 2, 1]
print(insertionSort(vetor))