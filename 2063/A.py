for t in range(int(input())):
    l, r = map(int, input().split(" "))
    if l == r == 1:
        print(1)
    else:
        print(r-l)
