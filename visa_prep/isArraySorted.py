def a(k):
    for i in range(1,len(k)):
        if k[i]<k[i-1]:
            return False
    return True
z=int(input())
k=list(map(int,input().split()))
print("true" if a(k) else "false")
