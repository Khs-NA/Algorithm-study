n = int(input())  # 색종이의 개수
total_len = 0

paper = [[0] * 101 for _ in range(101)]  # 100x100 크기의 종이를 만듭니다.

# 색종이를 붙이는 부분을 1로 마킹합니다.
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 색종이 1칸 주위에 0이 존재한다면 그건 변이라는 소리니깐 total_len에 1추가
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            # 색종이 1칸 주위에 0이 1개 존재한다면 그건 변이라는 소리니깐 total_len에 1추가
            if (i > 0 and paper[i-1][j] == 0) or (i < 100 and paper[i+1][j] == 0) or (j < 100 and paper[i][j+1] == 0) or (j > 0 and paper[i][j-1] == 0):
                total_len += 1
            # 색종이 1칸 주위에 0이 2개 존재한다면 그건 모서리라는 소리니깐 total_len에 하나 더 1추가
            if ((i > 0 and paper[i-1][j] == 0) and (j < 100 and paper[i][j+1] == 0)) or ((i > 0 and paper[i-1][j] == 0) and (j > 0 and paper[i][j-1] == 0)) or ((i < 100 and paper[i+1][j] == 0) and (j < 100 and paper[i][j+1] == 0)) or ((i < 100 and paper[i+1][j] == 0) and (j > 0 and paper[i][j-1] == 0)):
                total_len += 1

print(total_len)
