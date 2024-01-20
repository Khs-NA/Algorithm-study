
# 격자판 생성
grid = [[0] * 101 for _ in range(101)]

# 입력 개수
n = int(input().strip())

# 색종이 번호별로 순서대로 처리
for paper_number in range(1, n + 1):
    x, y, width, height = map(int, input().split())

    # 색종이 붙이기
    for i in range(x, x + width):
        for j in range(y, y + height):
            grid[i][j] = paper_number

# 각 색종이의 면적 계산 및 출력
for paper_number in range(1, n + 1):
    area = sum(row.count(paper_number) for row in grid)
    print(area)
