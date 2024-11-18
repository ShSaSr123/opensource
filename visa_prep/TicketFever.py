j=int(input())
for _ in range(j):
    a,b=map(int,input().split())
    if a>b:
        print(a-b)
    else:
        print(0)
