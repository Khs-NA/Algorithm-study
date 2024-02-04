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
    # 대각선1은 i와 j가 같으면 됩니다. (좌상단 -> 우하단)
    for i in range(N):
        sum_arr = []
        j = i
        sum_arr.append((input_arr[i][j]))
        total.append((sum(sum_arr)))

    # 대각선 2는 i가 뒤에서부터 감소하면 됩니다. (우상단->좌하단)
    for i in range(N-1,-1,-1):    #99 98 97
        sum_arr = []
        j = i
        sum_arr.append((input_arr[i][j]))
        total.append((sum(sum_arr)))

    print(f'#{T} {max(total)}')

    # [0,5] -> [1,4] -> [2,3] -> [3,2] -> [4,1] -> [5,0]
    # i는 증가 , j는 감소
    # tmp = 0
    # for i in range(100):
    #     tmp += arr[i][99-i]
    # if result < tmp:
    #     result = tmp


    # tmp = 0
    # for i in range(100):
    #     for j in range(100):
    #         if i == j:
    #             tmp += arr[i][j]
    # if result < tmp:
    #     result = tmp
