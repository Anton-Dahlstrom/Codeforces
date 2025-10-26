for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    freq = [0]*(n+1)
    for num in arr:
        freq[num] += 1
    unique = False
    for f in freq:
        if f == 1:
            unique = True
            break
    if not unique:
        print(0)
        continue

    l = 0
    cur = 0
    best = 0
    bestl, bestr = 0, 0
    for r in range(n):
        if freq[arr[r]] == 1:
            cur += 1
            if cur > best:
                best = cur
                bestl = l
                bestr = r
        else:
            l = r+1
            cur = 0

    print(f"{bestl+1} {bestr+1}")
