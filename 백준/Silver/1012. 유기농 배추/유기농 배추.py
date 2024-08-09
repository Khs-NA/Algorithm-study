# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        x_, y_ = stack.pop()
        # 예외처리
        if not (0<= x_ < M and 0<= y_ < N) or visited[y_][x_] or not arr[y_][x_]:
            continue

        visited[y_][x_] = True
        for k in range(4):
            nx = x_ + dx[k]
            ny = y_ + dy[k]
            stack.append((nx, ny))






tc = int(input())
for _ in range(tc):
    M, N, K = map(int,input().split())

    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int,input().split())
        arr[y][x] = 1

    warm = 0
    for j in range(N):
        for i in range(M):
            if arr[j][i] == 1 and not visited[j][i]:
                dfs(i, j)
                warm += 1

    print(warm)