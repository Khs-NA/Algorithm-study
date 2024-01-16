# find_dwarfs 함수는 9명의 난쟁이 중 2명을 선택하고,
# 선택된 두 명을 제외한 나머지 7명의 키를 selected_heights 에 저장.
# selected_heights 의 합이 100 이되면 리스트를 정렬하고 반환.


def find_dwarfs(heights):
    for i in range(9):
        for j in range(i + 1, 9):
            selected_heights = [heights[k] for k in range(9) if k != i and k != j]

            if sum(selected_heights) == 100:
                return sorted(selected_heights)




# 난쟁이들의 키 입력
heights = [int(input()) for _ in range(9)]

# 일곱 난쟁이를 찾아 정렬된 키를 출력
result = find_dwarfs(heights)
for height in result:
    print(height)
