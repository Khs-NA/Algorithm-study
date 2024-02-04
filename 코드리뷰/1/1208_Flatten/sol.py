# 1208_Flatten

import sys
sys.stdin = open('input.txt')

def Flatten_max_sub_min(dump):

    arr = list(map(int, input().split()))
    for _ in range(dump):
        max_height_index = arr.index(max(arr))
        min_height_index = arr.index(min(arr))

        arr[max_height_index] -= 1
        arr[min_height_index] += 1

    return (max(arr)- min(arr))


    # # while문 사용하기
    # height = list(map(int, input().split()))
    # while dump > 0:
    #     max_height_index = height.index(max(height))
    #     min_height_index = height.index(min(height))
    #
    #     height[max_height_index] -= 1
    #     height[min_height_index] += 1
    #
    #     dump -= 1
    # return (max(height) - min(height))



T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = Flatten_max_sub_min(n)
    print(f'#{test_case} {result}')




