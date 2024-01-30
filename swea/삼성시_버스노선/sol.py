# SWEA 6485번: 삼성시의 버스 노선
import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 정류장의 수
    bus_stops = [0] * 5001  # 정류장을 지나가는 버스 노선의 횟수를 저장할 리스트

    # 버스 노선 정보 입력
    for _ in range(N):
        A, B = map(int, input().split())
        for stop in range(A, B + 1):
            bus_stops[stop] += 1

    # 출력
    P = int(input())  # 조회할 정류장 수
    results = []
    for _ in range(P):
        C = int(input())
        results.append(bus_stops[C])

    print(f'#{test_case}', ' '.join(map(str, results)))
