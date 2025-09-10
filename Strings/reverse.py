s=list('harsha')
n=len(s)
for i in range(n//2):
    s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
print("".join(s))