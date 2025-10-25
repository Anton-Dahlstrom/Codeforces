for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    one = False
    two = False
    for i in range(0, n):
        if nums[i] != 0:
            if nums[i-1] == 0 and one:
                two = True
                break
            one = True
    if two:
        print("2")
    elif not one:
        print("0")
    else:
        print("1")
