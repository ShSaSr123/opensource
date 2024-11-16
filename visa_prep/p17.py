a,b=map(int,input().split())
if 1<=a<10 and 1<=b<10**9:
    t=(b+99)//100
    c = max(0,t-a)
    print(c)
