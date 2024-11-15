p,q,r,s=list(map(int,input().split()))
if p+q>=s or p+r>=s or q+r>=s:
    print("YES")
else:
    print("NO")
