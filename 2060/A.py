for t in range(int(input())):
    nums = list(map(int, input().split(" ")))

    if nums[1] == nums[3] and nums[1] == nums[2]:
        val = 0
    elif nums[2]-nums[1] == nums[3]-nums[2]:
        val = nums[2]-nums[1]
    else:
        val = nums[0]+nums[1]

    nums.insert(2, val)
    res = 0
    for i in range(2, 5):
        if nums[i] == nums[i-1]+nums[i-2]:
            res += 1
    print(res)
