n = int(input())  # 색종이의 개수
total_len = 0

paper = [[0] * 101 for _ in range(101)]  # 101x101 크기의 종이를 만듭니다.

# 색종이를 붙이는 부분을 1로 마킹합니다.
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 각 좌표에 대해 상하좌우를 확인하여 색종이가 닿는 부분을 더합니다.
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            total_len += 4
            if i > 0 and paper[i - 1][j] == 1:
                total_len -= 2
            if j > 0 and paper[i][j - 1] == 1:
                total_len -= 2

print(total_len)
