def s(a,b):
    v=b[1:]+b[:1]
    return v
a=int(input())
b=list(map(int,input().split()))
sq=s(a,b)
print(" ".join(map(str,sq)))
