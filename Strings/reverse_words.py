n=('Hi i am Harsha').split()
l=len(n)
for i in range(l//2):
    n[i],n[l-i-1]=n[l-i-1],n[i]
print(".".join(n))