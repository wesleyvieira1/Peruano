def quickSort(vetor, l, h):
    if(h>l):
        pivo = particao(vetor, l, h)
        quickSort(vetor, l, pivo-1)
        quickSort(vetor, pivo+1, h)
    return vetor

def particao(vetor, l, h):
    pivo = h
    pa = l
    for i in range(l, h):
        if(vetor[i] < vetor[pivo]):
            (vetor[i], vetor[pa]) = (vetor[pa],vetor[i])
            pa += 1
    (vetor[pivo], vetor[pa]) = (vetor[pa], vetor[pivo])
    print(vetor)
    return pa

vetor = [5,3,4,2,1]
l = 0
h = len(vetor)-1
print(quickSort(vetor, l, h))