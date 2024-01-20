# 격자판 크기
grid_size = 1001

# 격자판 초기화
grid = [[0] * grid_size for _ in range(grid_size)]

# 입력 개수
n = int(input().strip())

# 색종이 번호별로 순서대로 처리
for paper_number in range(1, n + 1):
    x, y, width, height = map(int, input().split())

    # 색종이 붙이기
    for i in range(x, x + width):
        for j in range(y, y + height):
            # 겹치는 부분에서 가장 큰 색종이 번호로 업데이트
            grid[i][j] = max(grid[i][j], paper_number)

# 각 색종이의 면적 계산 및 출력
for paper_number in range(1, n + 1):
    area = sum(row.count(paper_number) for row in grid)
    print(area)
