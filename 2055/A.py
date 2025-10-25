for t in range(int(input())):
    n, a, b = map(int, input().split(" "))
    if (a-b) % 2 == 0:
        print("YES")
    else:
        print("NO")
