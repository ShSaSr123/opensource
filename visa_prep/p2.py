s,p,r = map(int,input().split())

if(s>r):
    print(0)
elif(r>=(s+p)):
    print(2)
else:
    print(1)
