import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    max = 0
    min = 999999999999999999999
    for i in range(N):
        if max < arr[i]:
            max = arr[i]

        if min > arr[i]:
            min = arr[i]
        max_min = max - min
    print(f'#{test_case} {max_min}')