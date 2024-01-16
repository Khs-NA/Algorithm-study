def find_nearest_sum(nan_list, target):
    closest_sum = 0
    selected_numbers = []
    for i in range(len(nan_list)):
        for j in range(i+1, len(nan_list)):
            for k in range(j+1, len(nan_list)):
                for l in range(k+1, len(nan_list)):
                    for m in range(l+1, len(nan_list)):
                        for n in range(m+1, len(nan_list)):
                            for o in range(n+1, len(nan_list)):
                                current_sum = nan_list[i] + nan_list[j] + nan_list[k] + nan_list[l] + nan_list[m] + nan_list[n] + nan_list[o]
                                
                                if current_sum <= target and current_sum > closest_sum:
                                    closest_sum = current_sum
                                    selected_numbers = [nan_list[i], nan_list[j], nan_list[k], nan_list[l], nan_list[m], nan_list[n], nan_list[o]]
    return selected_numbers

# 예시
target = 100
nan_list = [int(input()) for _ in range(9)]


result = find_nearest_sum(nan_list, target)


# 오름차순 정렬
n = len(result)

for i in range(0, n-1):
    least = i
    for j in range(i+1, n):
        if result[least] > result[j]:
            least = j
    result[i], result[least] = result[least], result[i]

# 한줄씩 출력
for number in result:
    print(number)