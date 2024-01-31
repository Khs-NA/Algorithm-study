import sys
sys.stdin = open('input.txt')

# 1. 칠하는 색상 갯수만큼 반복
# 2. 색상 칠하기, 칠하는 곳에 색상 코드 값만큼 입력, 만약 이때 영역에 같은 코드 값이 들어오면 주의
# 3. 겹치는 부분 카운트, 보라색 코드 값을 가지는 영역 카운트

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    paper = [[0]*10 for _ in range(10)] # 9*9 배열을 만들기 위해서는 10*10해준다.
    color_num = int(input())
    for color_tc in range(color_num):
        color_arr = list(map(int,input().split()))
        color_val = color_arr[-1]
        r1 = color_arr[0]
        c1 = color_arr[1]
        r2 = color_arr[2]
        c2 = color_arr[3]
        # print(color_val,r1,r2,c1,c2)

        for length in range(r1,r2+1 ):
            for high in range(c1,c2+1):
                if paper[length][high] != color_val:
                    paper[length][high] += color_val
        violet = 0
        for i in range(9):
            for j in range(9):
                if paper[i][j] == 3:
                    violet += 1

    print(f'#{test_case} {violet}')
