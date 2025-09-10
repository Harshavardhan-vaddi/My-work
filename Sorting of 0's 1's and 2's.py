arr = list(map(int, input().split()))
z, o, t = 0, 0, 0

for i in arr:
    if i == 0:
        z += 1
    elif i == 1:
        o += 1
    elif i == 2:
        t += 1

print(('0 ' * z) + ('1 ' * o) + ('2 ' * t))
