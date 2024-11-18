def k(a,b):
    q=set()
    w=[]
    for i in b:
        if i not in q:
            w.append(i)
            q.add(i)
    return w
a=int(input())
b=list(map(int,input().split()))
l=k(a,b)
print(" ".join(map(str,l)))
