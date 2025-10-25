tests = int(input())

for t in range(tests):
    n, m, k = map(int, input().split(" "))
    if n > k+1:
        input()
        input()
        print("0"*m)
        continue
    if n == k:
        input()
        input()
        print("1"*m)
        continue
    lists = list(map(int, input().split(" ")))
    known = set(map(int, input().split(" ")))
    res = "0"*m
    found = False
    for i in range(len(lists)):
        if lists[i] not in known:
            found = True
            break
    if found:
        res = res[:i] + "1" + res[i+1:]
    print(res)
