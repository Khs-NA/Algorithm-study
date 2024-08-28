def main():
    for i in range(len(Arr)):
        for j in range(i,len(Arr)):
            if Arr[j] > Arr[i]:
                dp[j] = max(dp[j],dp[i] + 1)

    print(max(dp))


if __name__=='__main__':
    N = int(input())
    Arr = list(map(int,input().split()))
    dp = [1] * len(Arr)
    main()