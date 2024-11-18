def m(a,b):
    return(a & (1<<(b-1))) != 0
a=int(input().strip())
b=int(input().strip())
print("true" if m(a,b) else "false")
