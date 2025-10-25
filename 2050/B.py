
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    if sum(nums) % n:
        print("NO")
        continue
    uneven = False
    sums = [0, 0]
    for s in range(0, 2):
        total = 0
        count = 0
        for i in range(s, n, 2):
            total += nums[i]
            count += 1
        if total % count:
            uneven = True
            break
        sums[s] = total // count
    if uneven or sums[0] != sums[1]:
        print("NO")
    else:
        print("YES")
