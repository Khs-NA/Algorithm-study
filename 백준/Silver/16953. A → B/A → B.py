def main(a, b, cnt):
    global ans

    if int(a) == int(b):
        ans = cnt
        return 
    elif int(a) > int(b):
        return -1

    result1 = main(int(a*2), b, cnt + 1)
    result2 = main(int(str(a) + '1'), b, cnt + 1)

    if result1 == -1 and result2 == -1:
        return -1


if __name__ == '__main__':
    A, B = map(int, input().split())
    ans = 0
    result = main(A, B, 1)

    if result == -1:
        print(-1)
    else:
        print(ans)
