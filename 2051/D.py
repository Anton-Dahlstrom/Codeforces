def pairsGreaterThanX(arr, x):
    n = len(arr)
    j = 0
    res = 0
    for i in range(n-1, -1, -1):
        if arr[i] + arr[i] > x:
            res -= 1
        while arr[i] + arr[j] <= x:
            j += 1
            if j == n:
                return res//2
        res += (n-j)

    return res//2


for t in range(int(input())):
    n, x, y = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    nums.sort()
    s = sum(nums)
    left = pairsGreaterThanX(nums, s-x)
    right = pairsGreaterThanX(nums, s-y-1)
    print(right - left)
