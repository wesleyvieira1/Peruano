def FunAckermann(m,n,p):
    if p==0:
        return m+n
    elif p==1:
        if n==0:
            return 0
        else:
            return m*n
    elif p==2:
        if n==0:
            return 1
        else: 
            return m**n
    elif p>2:
        if n==0:
            return m
        else:
            return FunAckermann(m,FunAckermann(m,n-1,p),p-1)
m,n,p = map(int,input().split())
while m>=0 and n>=0 and p>=0:
    if m==0 and n==0 and p==0:
        print(FunAckermann(m,n,p))
        break
    else:
        print(FunAckermann(m,n,p))
    m,n,p = map(int,input().split())