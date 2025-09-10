# Brute Force Approach
arr=list(map(int,input().split()))
a=list(set(arr))
for i in a:
    if arr.count(i)==1:
        print(i)
        break

# Optimal Approach
arr=list(map(int,input().split()))
xor=0
for i in arr:
    xor^=i
print(xor)