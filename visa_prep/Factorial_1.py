def a(k):
    f=1
    for i in range(1,k+1):
        f*=i
    return f    
v=int(input())
print(a(v))
