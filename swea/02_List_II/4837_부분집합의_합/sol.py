import sys
sys.stdin = open('input.txt')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = list(map(int,input().split()))
+
    arr = list(range(1,13))
    n = len(arr)
    count = 0
    # 전체 부분집합 구하기
    for i in range(1<<n): 
        lst = []
        for j in range(n):
            if i & (1<<j):
                lst.append(arr[j])
        # 부분집합의 원소가 N개 , 원소의 합이 K 일 경우 카운트
        if (len(lst) == N and sum(lst) == K):
            count += 1



    print(f'#{test_case} {count}')


