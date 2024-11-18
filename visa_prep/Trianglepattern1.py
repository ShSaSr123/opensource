a=int(input())
z=1
for i in range(1,a+1):
    r=[str(z+j) for j in range(i)]
    print(" ".join(r))
    z+=i
