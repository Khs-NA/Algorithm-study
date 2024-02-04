import sys
sys.stdin = open("input_풍선팡.txt")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    row , column = (map(int, input().split()))
    arr = [list(map(int,input().split())) for _ in range(row)]

    di = [0, -1, 1, 0]
    dj = [-1, 0, 0, 1]
    total_sum = []
    for i in range(row):
        for j in range(column):
            pang = []
            if arr[i][j] > 0:
                pang.append(arr[i][j])
                for k in range(4):
                    for v in range(1, arr[i][j] + 1):
                        ni = i + v*di[k]
                        nj = j + v*dj[k]
                        if 0 <= ni < row and 0 <= nj < column:
                            # 점수 합산
                            pang.append(arr[ni][nj])

                    total_sum.append(sum(pang))

    print(f'#{test_case} {max(total_sum)}')