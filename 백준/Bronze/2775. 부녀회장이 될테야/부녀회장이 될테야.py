tc = int(input())  # 테스트 케이스 수 입력


result = []
for _ in range(tc):
    floor = int(input())  # 층 수 입력
    room = int(input())  # 호 수 입력

    apt = [[0] * 22 for _ in range(22)]  # 아파트 배열 초기화

    for i in range(floor + 1):  # 층을 기준으로 반복
        for j in range(1, room + 1):  # 방 번호를 기준으로 반복
            if i == 0:
                apt[i][j] = j  # 0층에서는 방 번호가 그대로 값
            else:
                apt[i][j] = apt[i][j - 1] + apt[i - 1][j]  # 위층과 왼쪽 값을 더함

    result.append(apt[floor][room])


for i in result:
    print(i)