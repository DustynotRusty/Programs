def checkBit(n, k):
    new_num = n >> k
    return (new_num & 1)


def tripleTrouble(n, ar):
    ans = 0
    for i in range(30):
        c = 0
        for j in range(n):
            if (checkBit(ar[j], i) == True):
                c += 1
        if (c % 3 != 0):
            ans += 1 << i
    print(ans)


t_c = int(input())
for i in range(t_c):
    n = int(input())
    ar = list(map(int, input().strip().split()))[:n]
    tripleTrouble(n, ar)
