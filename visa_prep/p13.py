a,b,c=map(int,input().split())
tr = a*b
ta = c*24*60
if tr<=ta:
    print("YES")
else:
    print("NO")
