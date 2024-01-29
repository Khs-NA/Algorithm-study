
import sys
sys.stdin = open("sample_input.txt", "r")


def section_sum(length, pick):
    result_sum = 0
    result_sub = 99999999999999999
    arr = list(map(int, input().split()))
    for i in range(length - pick + 1):
        arr_sum = sum(arr[i:i + pick])

        if arr_sum > result_sum:
            result_sum = arr_sum
        if arr_sum < result_sub:
            result_sub = arr_sum
    return result_sum - result_sub

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    fir_arr = list(map(int, input().split()))
    lenght = int(fir_arr[0])
    pick = int(fir_arr[-1])
    result = section_sum(lenght,pick)
    print(f'#{test_case} {result}')

