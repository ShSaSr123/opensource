x,y,z = map(int,input().split())
if(y>=z):
    print(0)
else:
    m = (z - y) // x
    print(m)
