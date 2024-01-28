# import sys
# sys.stdin = open("input.txt")


# 1. 이론상 가장 많은 롤 케이크를 가져가는 사람
# strat, end = input() 받는다. 그 후 end - start + 1 을 해서 가장 큰 값을 가지는 사람이 정답

L = int(input())
people = int(input())

cake = [1]*(L+1)
max1 = 0
max2 = 0
max1_i = 0
max2_i = 0


for n in range(1,people+1):  # 실제 방청객의 번호
     s , e = map(int, input().split())
     if max1 < (e - s +1):    # 원한 개수가 가장 큰 값이면 갱신
         max1, max1_i = (e-s+1), n

     count = sum(cake[s:e+1]) # 실제 n번 방청객이 받은 케이크 갯수
     if max2 < count:
        max2, max2_i = count, n
     cake[s:e+1] = [0] * (e - s +1)

print(max1_i)
print(max2_i)

