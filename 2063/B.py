import heapq


for t in range(int(input())):
    n, l, r = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    left = []
    mid = []
    right = []
    arr = left
    multiplier = 1
    for i in range(len(nums)):
        if i == l-1:
            arr = mid
            multiplier = -1
        elif i == r:
            arr = right
            multiplier = 1
        heapq.heappush(arr, nums[i] * multiplier)
    start = sum(mid) * -1
    rightswap = 0
    leftswap = 0
    while mid and (left or right):
        midval = heapq.heappop(mid) * -1
        if left:
            leftval = heapq.heappop(left)
            if leftval < midval:
                leftswap += (midval - leftval)
            else:
                left = []
        if right:
            rightval = heapq.heappop(right)
            if rightval < midval:
                rightswap += (midval - rightval)
            else:
                right = []
    print(start - max(rightswap, leftswap))
