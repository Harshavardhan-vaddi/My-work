arr = list(map(int, input().split()))
k = int(input())
arr.sort()

i = 0
j = len(arr) - 1
found = False

while i < j:
    curr_sum = arr[i] + arr[j]
    if curr_sum == k:
        print("Pair:", arr[i], arr[j])
        found = True
        break
    elif curr_sum < k:
        i += 1
    else:
        j -= 1

if not found:
    print(-1, -1)
