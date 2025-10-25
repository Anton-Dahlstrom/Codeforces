for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    modes = set()
    prev = 1
    res = []
    for num in nums:
        if num not in modes:
            modes.add(num)
            res.append(str(num))
        else:
            for j in range(prev, n+1):
                if j not in modes:
                    modes.add(j)
                    res.append(str(j))
                    prev = j
                    break
        if len(modes) == n:
            prev = 1
            modes = set()
    print(" ".join(res))
