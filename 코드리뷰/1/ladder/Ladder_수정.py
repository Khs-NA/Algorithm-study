# SWEA 1210.Ladder 1
import sys
sys.stdin = open("input_ladder.txt")

def search(i,j):
    visited = [[0] * 100 for _ in range(100)]
    orginal_j = j
    while i != 99:
        for dir in [(1, 0), (0, -1), (0, 1)]:
            ni = i + dir[0]
            nj = j + dir[1]
            if 0 <= ni < 100 and 0 <= nj < 100 :
                if arr[ni][nj] == 1:
                    if not visited[ni][nj]:
                        i, j = ni, nj
                        visited[i][j] = 1
                if arr[ni][nj] == 2:
                    return orginal_j
    # 도착점 도착은 못했지만 i == 99가 되어서 조사가 끝나면 None을 return 했다...
    return


T = int(input())

for test_case in range(1, 10):

    arr = [list(map(int, input().split())) for _ in range(100)]
    # 최종결과값
    result = 0

    # 사다리의 크기 == 100 * 100
    for j in range(100):
        # 출발 지점:
        if arr[0][j] == 1:
            # 출발 시점의 j 좌표 == 0으로 가정
            result = search(0,j)
            if result != None:
                break

    print(result)