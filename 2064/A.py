
for t in range(int(input())):
    n = int(input())
    binstr = "0" + input()
    res = 0
    for i in range(1, n+1):
        if binstr[i] != binstr[i-1]:
            res += 1
    print(res)
