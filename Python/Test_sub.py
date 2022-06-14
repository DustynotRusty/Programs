t_c = int(input())
for _ in range(t_c):
    a, b = map(int, input().split())

    hcf = 1

    for i in range(2, a+1):
        if(a % i == 0 and b % i == 0):
            hcf = i
    lcm = int((a*b)/(hcf))
    print(lcm, hcf)
