def maxSubarraySum(arr, n):
    maxi = arr[0] 
    sum = 0

    for i in arr:
        sum += i
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0

    return maxi

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [4, -1, 2, 1]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum) 