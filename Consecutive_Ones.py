arr=list(map(int,input().split()))
c,m=0,0
for i in arr:
    if i==1:
        c+=1
    else:
        m=max(c,m)
        c=0
    m=max(c,m)
print(m)
