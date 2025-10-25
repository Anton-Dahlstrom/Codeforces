def checkCombo(s, twos, threes):
    for i in range(0, twos+1):
        for j in range(0, threes+1):
            if not (s + (i*2) + (j*6)) % 9:
                return "YES"
    return "NO"


for _ in range(int(input())):
    inp = input()
    s = 0
    if len(inp) > 2000:
        prev = 0
        l = 0
        while True:
            r = min(len(inp), l+1000)
            s += int(inp[l:r])
            s %= 9
            if r == len(inp):
                break
            l = r
    else:
        s = int(inp) % 9
    if not s % 9:
        print("YES")
        continue
    twos = 0
    threes = 0
    for c in inp:
        if c == "2":
            twos += 1
        elif c == "3":
            threes += 1
        if twos > 4 and threes > 8:
            break
    print(checkCombo(s, twos, threes))
