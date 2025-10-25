for t in range(int(input())):
    n = int(input())

    def dfs(cur, n):
        if len(cur) == n:
            if int(cur) % 66 == 0:
                return cur
            return False
        res = dfs(cur+"3", n)
        if res:
            return res
        res = dfs(cur+"6", n)
        if res:
            return res
        return False

    res = dfs("", n)
    if res:
        print(res)
    else:
        print("-1")
