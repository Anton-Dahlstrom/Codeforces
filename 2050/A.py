
for _ in range(int(input())):
    n, m = map(int, input().split(" "))
    res = 0
    total = m
    for i in range(n):
        size = len(input())
        total -= size
        if total >= 0:
            res += 1
    print(res)
