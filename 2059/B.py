for t in range(int(input())):
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    if n == k:
        count = 0
        for i in range(1, n, 2):
            count += 1
            if nums[i] != count:
                break
            else:
                if i == n-1:
                    count += 1
        print(count)

    else:
        ans = 2
        for i in range(1, n-k+2):
            if nums[i] != 1:
                ans = 1
                break
        print(ans)
