for t in range(int(input())):
    n = int(input())
    materials = list(map(int, input().split(" ")))
    artifact = list(map(int, input().split(" ")))
    transformations = 0
    for i in range(n):
        if materials[i] < artifact[i]:
            transformations += artifact[i] - materials[i]
    possible = True
    for i in range(n):
        diff = max(artifact[i] - materials[i], 0)
        if (materials[i] + diff) - (transformations - diff) < artifact[i]:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")
