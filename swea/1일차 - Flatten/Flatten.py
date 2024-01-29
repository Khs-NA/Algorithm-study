# import sys
# sys.stdin = open("input.txt", "r")

def Flatten_max_sub_min(n):

    arr = list(map(int, input().split()))
    for _ in range(n):
        max_height_index = arr.index(max(arr))
        min_height_index = arr.index(min(arr))

        arr[max_height_index] -= 1
        arr[min_height_index] += 1
    return (max(arr)- min(arr))

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = Flatten_max_sub_min(n)
    print(f'#{test_case} {result}')


# for tc in range(1, 11):
#     dump = int(input())
#     box = list(map(int, input().split()))
#     for i in range(dump):
#         box[box.index(max(box))] -= 1
#         box[box.index(min(box))] += 1
#     print(f'#{tc} {max(box)-min(box)}')
