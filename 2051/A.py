tests = int(input())

for t in range(tests):
    n = int(input())
    monocarp = list(map(int, input().split(" ")))
    stereocarp = list(map(int, input().split(" ")))
    res = 0
    for i in range(n-1):
        if monocarp[i] > stereocarp[i+1]:
            res += monocarp[i] - stereocarp[i+1]
    res += monocarp[-1]
    print(res)
