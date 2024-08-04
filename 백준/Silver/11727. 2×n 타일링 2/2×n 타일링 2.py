n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    sqr = [0] * (n+1)
    sqr[1] = 1
    sqr[2] = 3
    for i in range(3, n+1):
        sqr[i] = sqr[i-1] + 2 * sqr[i-2]

    print(sqr[n] % 10007)
