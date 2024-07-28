def make_one(x,cnt):
    global result

    if cnt > result:
        return 

    if x == 1:
        result = min(cnt, result)
        return result

    if x%3 == 0:
        make_one(x//3, cnt + 1)
    if x%2 == 0:
        make_one(x//2, cnt + 1)

    make_one(x - 1, cnt + 1)



X = int(input())

result = 99999999999999
make_one(X, 0)

print(result)