# 1209_sum
import sys
sys.stdin = open('input.txt')


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    N = 100
    input_arr = []
    # input.txt가 100줄이므로 100번 반복해서 입력해줍니다.
    for i in range(100):
        input_arr.append(list(map(int, input().split())))

    total = []

    # 가로 줄 합 N개를 total 리스트에 추가해줍니다.
    for i in range(N):
        sum_arr = []
        for j in range(N):
            sum_arr.append((input_arr[i][j]))
        total.append((sum(sum_arr)))

    # 세로 줄 합 N개를 total 리스트에 추가해줍니다.
    for j in range(N):
        sum_arr = []
        for i in range(N):
            sum_arr.append((input_arr[i][j]))
        total.append((sum(sum_arr)))

    # 대각선을 total 리스트에 추가해줍니다.
    # 대각선1은 i와 j가 같으면 됩니다.
    for i in range(N):
        sum_arr = []
        j = i
        sum_arr.append((input_arr[i][j]))
        total.append((sum(sum_arr)))

    # 대각선 2는 j가 증가하고 i는 N - j 면 됩니다.
    for i in range(N-1,-1,-1):
        sum_arr = []
        j = N - i
        sum_arr.append((input_arr[i][j]))
        total.append((sum(sum_arr)))

    print(f'#{T} {max(total)}')


