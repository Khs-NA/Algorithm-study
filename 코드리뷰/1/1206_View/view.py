import sys
sys.stdin = open("input.txt", "r")

def sun_view(n):
    arr = list(map(int,input().split()))
    sun_sum = 0
    if (n>=4 and n<= 1000):
        for building in range(len(arr[1:])-1): #  range 범위가 이게 맞나?
            if (arr[building] > arr[building-1] and arr[building] > arr[building-2] and arr[building] > arr[building+1] and arr[building] > arr[building+2]): # 진짜 무식하게 때려넣음
                sec = max(arr[building-1],arr[building-2] ,arr[building+1] , arr[building+2])
                sun_sum += (arr[building]-sec)
        return sun_sum


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input()) # 건물 갯수
    result = sun_view(n)
    print(f'#{test_case} {result}')


# ----------------------------------------------
# 수업시간
# 구간합 문제이다.
# 5개씩 묶어서 판별하자.

# for test_case in range(1, 11):
#     N = int(input())
#     data = list(map(int, input().split()))
#     result = 0
#     # 최종 결괏값 : 조망권 총 개수
#     # 전부 다 조사
#     # 앞 뒤 2칸은 건물 없음이 조건(조사범위에서 앞뒤 2개씩 뺌)
#     for i in range(2, N-2): # 왼쪽, 오른쪽 2칸 제외한 범위
#         # 임시 변수 i -> data[i] 번째 조사 대상 건물을 말한다.
#         # 항상 5개씩 조사
#         # 각 건물의 최대 높이 255
#         min_value = 256
#         for j in range(5):
#             '''
#             i = 3 , j == 0 | 1  = 3 - 2 + 0
#             i = 3 , j == 1 | 2  = 3 - 2 + 1
#             i = 3 , j == 2 | 3  = 3 - 2 + 2
#             i = 3 , j == 3 | 4  = 3 - 2 + 3
#             i = 3 , j == 4 | 5  = 3 - 2 + 4
#             '''
#             # 나와 나를 비교하는 상황은 무시
#             # if j == 2 : continue
#             if j != 2:
#                 if data[i] - data[i - 2 + j] < min_value:
#                     min_value = data[i] - data[i - 2 + j]
#         # 조망권이 양수인 경우에만
#         if min_value > 0 :
#             result += min_value
#     print(result)


# ------------------------------
# # 방법 2
# # 조사 범위는 동일
# for tc in range(1, 11):
#     N = int(input())
#     data = list(map(int, input().split()))
#     # print(data)
# 
#     # 최종 결괏값 : 조망권 총 개수
#     result = 0
# 
#     for i in range(2, N - 2):
#         # 임시변수 i를 기준으로 5개의 범위선정
#         # 4개의 이웃중 제일 큰 이웃찾기
#         max_neighbor = 0
#         for j in range(i - 2, i + 3):ㄴ
#             # 나랑 나는 조사 안함
#             if i == j: continue
#             # j번째가 제일 큰 애들중에, 조사 대상 i보다 작은애들
#             if data[j] < data[i] and max_neighbor < data[j]:
#                 max_neighbor = data[j]
#             # 주변 아파트가 조사대상보다 크다면 break
#             elif data[j] >= data[i]:
#                 max_neighbor = data[i]
#                 break
#         # 최종결괏값 = 나의 크기 - 내 이웃중 제일 큰애
#         # 조사 도중에 취소된 경우
#         result += data[i] - max_neighbor
#         # # j번째 위치가 조사대상 i번쨰보다 크거나 같으면 무시
#         # if data[j] >= data[i]: continue
#         # # j번째 위치가 조사대상 i번쨰보다 작다면
#         # if data[j] < data[i]:
#         #     # 조사대상 크기 - j번째 아파트 크기
#         #     temp = data[i] - data[j]
#     print(result)


#----------------------------------------
# 강사님이 추천한 학생 핵심 코드

# for n in range(2, N - 2):
#     n_list = heights[n - 2:n + 3]
#     
#     if n_list[2] == max(n_list):
#         now = n_list.pop(2)
#         count += (now - max(n_list))
#         
        