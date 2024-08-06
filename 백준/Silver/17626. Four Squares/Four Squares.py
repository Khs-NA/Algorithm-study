def four_squares(target):
    # DP 배열을 초기화합니다. DP[i]는 숫자 i를 표현하는데 필요한 최소 제곱수의 개수입니다.
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # 0을 표현하는데 필요한 제곱수의 개수는 0개입니다.

    # 1부터 sqrt(target)까지의 제곱수를 사용하여 dp 배열을 갱신합니다.
    for i in range(1, int(target ** 0.5) + 1):
        square = i * i
        for j in range(square, target + 1):
            dp[j] = min(dp[j], dp[j - square] + 1)

    return dp[target]


n = int(input())
print(four_squares(n))
