def find_nearest_sum(card_list, target):
    closest_sum = 0

    for i in range(len(card_list)):
        for j in range(i+1, len(card_list)):
            for k in range(j+1, len(card_list)):
                current_sum = card_list[i] + card_list[j] + card_list[k]
                if current_sum <= target and current_sum > closest_sum:
                    closest_sum = current_sum

    return closest_sum


card_number, target = map(int, input().split())
card_list = list(map(int, input().split()))


result = find_nearest_sum(card_list, target)
print(result)