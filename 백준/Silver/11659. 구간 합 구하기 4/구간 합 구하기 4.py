import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적 합 배열 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

# 구간 합 계산 및 출력
for _ in range(M):
    start, end = map(int, input().split())
    sum_numbers = prefix_sum[end] - prefix_sum[start - 1]
    print(sum_numbers)
