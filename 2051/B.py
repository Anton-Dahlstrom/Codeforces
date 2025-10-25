tests = int(input())

for t in range(tests):
    inp = input().split(" ")
    n = int(inp[0])
    days = list(map(int, inp[1:]))
    walked = 0
    daysum = sum(days)
    res = n//daysum * 3
    n = n % daysum
    i = 0
    while walked < n:
        walked += days[i]
        res += 1
        if i == 2:
            i = 0
        else:
            i += 1
    print(res)
