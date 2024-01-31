# import sys
# sys.stdin = open('input.txt')


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    row, column = list(map(int,input().split())) # 행, 열
    arr = []
    for row_n in range(row):
        arr.append(list(map(int,input().split())))
    # arr 구현까지는 성공

    di = [0, -1, 1, 0]
    dj = [-1, 0, 0, 1]
    total_sum = []

    for i in range(1,row-1):
        for j in range(1,column-1):
            pang = []
            pang.append(arr[i][j])
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                pang.append(arr[ni][nj])

            total_sum.append(sum(pang))
    print(f'#{test_case} {max(total_sum)}')




