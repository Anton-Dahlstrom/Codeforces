for t in range(int(input())):
    n = int(input())
    s = input()
    l, r = 0, n
    if s[0] == "s":
        l += 1
    if s[-1] == "p":
        r -= 1
    pfound = False
    sfound = False
    valid = True
    for char in s[l:r]:
        if char == "p":
            pfound = True
        elif char == "s":
            sfound = True
        if pfound and sfound:
            valid = False
            print("NO")
            break
    if valid:
        print("YES")
