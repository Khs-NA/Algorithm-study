# 입력 받기
N, P = map(int, input().split())

# 나머지들을 저장할 배열 초기화
arr = []

# 초기 나머지 값은 N
rest = N

while True:
    # 다음 나머지 값 계산
    rest = rest * N % P
    
    # 계산한 나머지 값이 배열에 존재하면 break
    if rest in arr:
        break
    
    # 나머지 값을 배열에 추가
    arr.append(rest)

# 주기가 시작된 지점 이후의 길이를 계산하여 출력
print(len(arr)-arr.index(rest))