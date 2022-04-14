def fib(number,dic):
    if number<=1:
        return (number,1)
    else:
        #if number>1:
            if number in dic:
                return dic[number]
            else:
                val2, n2 = fib(number-2,dic)
                val1, n1 = fib(number-1,dic)
                dic[number] = val1 + val2, 1+n1+n2
                return (val1 + val2, 1+n1+n2)
dic = {}
N = int(input())
for i in range(0,N):
    number = int(input())
    (f,c) = fib(number,dic)
    print("fib({:}) = {:} calls = {:}".format(number,f,c-1))