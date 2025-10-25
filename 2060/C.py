for t in range(int(input())):
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    nums.sort()
    l, r = 0, n-1
    pairs = 0
    while l < r:
        if nums[l] + nums[r] == k:
            pairs += 1
            l += 1
            r -= 1
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1
    print(pairs)
