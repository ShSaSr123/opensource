def a(k):
    r=k<0
    k=abs(k)
    q=int(str(k)[::-1])
    if r:
        q=-q
    if q<-2**31 or q>2**31-1:
        return 0
    return q
k=int(input())
print(a(k))
