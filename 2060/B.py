for t in range(int(input())):
    n, m = map(int, input().split(" "))
    total = []
    for i in range(n):
        cards = list(map(int, input().split(" ")))
        for card in cards:
            total.append((card, i))

    total.sort()
    failed = False
    order = [-1]*n
    for i in range(len(total)):
        card, cow = total[i]
        if order[i % n] == -1:
            order[i % n] = cow+1
        else:
            if order[i % n] != cow+1:
                failed = True
                break
    if failed:
        print("-1")
    else:
        print(" ".join([str(n) for n in order]))
