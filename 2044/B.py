for t in range(int(input())):
    s = input()
    res = ""
    for char in reversed(s):
        if char == "p":
            res += "q"
        elif char == "q":
            res += "p"
        else:
            res += "w"
    print(res)
