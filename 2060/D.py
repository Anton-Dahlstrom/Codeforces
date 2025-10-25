for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    failed = False
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            failed = True
            break
        nums[i+1] -= nums[i]
        nums[i] = 0
    if failed:
        print("NO")
        continue
    print("YES")
