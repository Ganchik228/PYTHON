def Prost(n):
    otv = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            otv.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        otv.append(n)
    return otv

def Prost2(n,otv,k):
    if k>n:
        return otv
    if n%k==0:
        while n%k==0:
            otv.append(k)
            n=n/k
    Prost2(n,otv,k+1)
    return otv

k=2
otv=[]
n=int(input())
print(Prost2(n,otv,k))
print(Prost(n))