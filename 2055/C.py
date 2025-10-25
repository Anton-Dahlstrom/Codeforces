for t in range(int(input())):
    n, m = map(int, input().split(" "))
    steps = input() + "D"
    grid = [[] for _ in range(n)]
    rowsums = [0]*n
    colsums = [0]*m
    for row in range(n):
        grid[row] = list(map(int, input().split(" ")))
        for col in range(m):
            rowsums[row] += grid[row][col]
            colsums[col] += grid[row][col]
    rowgoal = max(rowsums)
    colgoal = max(colsums)

    x = 0
    row, col = 0, 0
    for step in steps:
        if step == "D":
            diff = x - rowsums[row]
            grid[row][col] += diff
            rowsums[row] += diff
            colsums[col] += diff
            row += 1
        else:
            diff = x - colsums[col]
            grid[row][col] += diff
            rowsums[row] += diff
            colsums[col] += diff
            col += 1

    if rowsums[n-1] != colsums[m-1]:
        x = rowsums[n-1] - colsums[m-1]
        row, col = 0, 0
        for step in steps:
            if step == "D":
                diff = x - rowsums[row]
                grid[row][col] += diff
                rowsums[row] += diff
                colsums[col] += diff
                row += 1
            else:
                diff = x - colsums[col]
                grid[row][col] += diff
                rowsums[row] += diff
                colsums[col] += diff
                col += 1

    for row in range(n):
        print(" ".join([str(n) for n in grid[row]]))
