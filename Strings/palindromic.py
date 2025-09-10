s='mom'
n=len(s)//2
flag=True
for i in range(n):
    if s[i]==s[len(s)-i-1]:
        continue
    else:
        flag=False
if flag:
    print("Palindrome")
else:
    print("Not")