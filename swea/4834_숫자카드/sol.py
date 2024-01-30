import sys
sys.stdin = open('input.txt')


def num_card(num):
    number = str(input())
    arr = [int(i) for i in number] # number 하나씩 쪼개기
    # print(arr)
    arr.sort() # count가 모두 동일할때, 최대값을 가지는 카드를 출력하기 위해서 오름차순으로 정렬

    count_max = 1
    card_max = 0
    for i in range(num):
        if arr.count(arr[i]) >= count_max:
            count_max = arr.count(arr[i])
            card_max = arr[i]


    return card_max , count_max


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    card, count = num_card(n)
    print(f'#{test_case} {card} {count}')

'''
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                 # 카드 장수
    card = input()
    counts = [0] * 10

    for i in card:                   # 각 카드의 숫자에 해당하는 카운트 증가
        counts[int(i)] += 1

    max_count = max(counts)          # 가장 많이 나온 카드 개수
    counts.reverse()                 # 카드 수가 동일하면 숫자가 높은 카드가 나와야하기 때문에
                                     # index메서드를 사용하기위해 리스트를 뒤집고
                                     # 가장 많이 나온 카드의 인덱스를 찾았다.

    max_card = 9 - counts.index(max_count)   # 한번 뒤집었기 때문에 제일 높게 나올 수 있는 카드가 9에서
                                             # 가장 많이 나온 카드의 인덱스를 빼면
                                             # 가장 많이 나온 카드의 숫자를 알 수 있다.


    print(f'#{test_case}', max_card, max_count)
'''