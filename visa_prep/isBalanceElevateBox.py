a=int(input())
s=list(map(int,input().split()))
z=[]
for i in range(a):
    l=sum(s[:i])
    r=sum(s[i+1:])
    b=abs(l-r)
    z.append(b)
print(" ".join(map(str,z)))
