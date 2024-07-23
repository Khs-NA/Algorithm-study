N, K = map(int, input().split())

Ai = []
for _ in range(N):
    Ai.append(int(input()))

Ai.sort(reverse=True)

coin_cnt = 0
for value in Ai:
    if K //value :
        coin_cnt += K//value
        K = K - (value * (K//value))

print(coin_cnt)