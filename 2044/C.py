for t in range(int(input())):
    m, a, b, c = map(int, input().split(" "))
    res = 0

    space = m
    space -= min(a, m)
    res += min(a, m)

    res += min(space, c)
    c -= min(space, c)

    space = m
    space -= min(m, b)
    res += min(m, b)
    res += min(space, c)
    print(res)
