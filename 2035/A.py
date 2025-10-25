for t in range(int(input())):
    n, m, r, c = map(int, input().split(" "))
    first = m - c
    second = (n-r) * (m+m-1)
    print(first+second)
