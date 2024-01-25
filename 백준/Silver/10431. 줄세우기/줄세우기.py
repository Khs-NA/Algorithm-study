n = int(input())

for test in range(1,n+1):
    arr = list(map(int, input().split()))[1:]
    count = 0
    # 핵심은 j와 j의 범위이다.
    # j 는 0부터 j까지가 진짜 중요
    for i in range(1,20):
        for j in range(i):
            if arr[i] < arr[j]:
                # before_j = lst[j]
                # lst[j] = lst[i]
                # lst[i] = before_j
                count += 1
    print(f'{test} {count}')