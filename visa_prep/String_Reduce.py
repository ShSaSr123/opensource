a=input()
z=''
x=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        x+=1
    else:
        z+=a[i-1]+str(x)
        x=1
z+=a[-1]+str(x)        
print(z)
