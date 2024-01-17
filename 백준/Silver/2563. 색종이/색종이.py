total_area = 0

n = int(input())  # n은 색종이의 개수

# paper = [[0] * 100 for _ in range(100)]  # 100x100 크기의 종이를 만듭니다.
paper = []
for i in range(100):
    row = [0] * 100  # 각 행을 만들고
    paper.append(row)  # 이를 이중 리스트에 추가



for _ in range(n):
    x, y = map(int, input().split())

    # 색종이를 붙이는 부분에 1로 마킹합니다.
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1


# area = sum(row.count(1) for row in paper)
for i in range(100):
    for j in range(100):
        total_area += paper[i][j]

print(total_area)



