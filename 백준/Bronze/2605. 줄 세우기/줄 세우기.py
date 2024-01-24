# 5
# 1 2 3 4 5 alst
# 0 1 1 3 2 lst
# 4 2 5 3 1

#첫 번째 학생 : 1
#두 번째 학생 : 2 1
#세 번째 학생 : 2 3 1
#네 번째 학생 : 4 2 3 1
#오 번째 학생 : 4 2 5 3 1



N = int(input())
lst = list(map(int, input().split()))
alst = [n for n in range(1, N+1)]
# alst_1 = list(range(1,N+1))




for i in range(N):
    n, t = lst[i], alst[i] # n : 몇 칸 앞으로 가는가?, t : 지금 내 값
    # 덮어씌우기
    for j in range(i,i-n,-1):
        alst[j] = alst[j-1]
    alst[i-n] = t

print(*alst) # 리스트 [ ] 제거해준다.