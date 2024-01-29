# import sys
# sys.stdin = open("input.txt", "r")

def sun_view(n):
    arr = list(map(int,input().split()))
    sun_sum = 0
    if (n>=4 and n<= 1000):
        for building in range(len(arr[1:])-1):
            if (arr[building] > arr[building-1] and arr[building] > arr[building-2] and arr[building] > arr[building+1] and arr[building] > arr[building+2]):
                sec = max(arr[building-1],arr[building-2] ,arr[building+1] , arr[building+2])
                sun_sum += (arr[building]-sec)
        return sun_sum

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input()) # 건물 갯수
    result = sun_view(n)
    print(f'#{test_case} {result}')