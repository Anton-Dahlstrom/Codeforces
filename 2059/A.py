from collections import Counter

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    ac = Counter(a)
    bc = Counter(b)
    if len(ac) + len(bc) >= 4:
        print("YES")
    else:
        print("NO")
