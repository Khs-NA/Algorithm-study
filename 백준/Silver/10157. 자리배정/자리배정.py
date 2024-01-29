C , R = map(int,input().split())
K = int(input())

if R*C < K: # 배정 불가능한 경우 0
    print(0)
else: # 배정하면서 k가 되면 좌표 출력
    di, dj = [1, 0 , -1 , 0] , [0, 1, 0, -1] # 방향
    # 주변을 1로 둘러싸면, 범위 체크 필요없음
    arr = [[1]*(C+2)] + [[1]+[0]*C+[1] for _ in range(R)] + [[1]*(C+2)] 
    '''
    1111111
    1000001
    1000001
    1000001
    1111111
    이렇게 배열을 만들어 준다
    '''
    ci, cj , dr = 1, 1, 0
    for n in range(1, K):
        arr[ci][cj] = n
        ni, nj = ci + di[dr], cj + dj[dr]
        if arr[ni][nj] == 0 : # 자리가 비어있으니 이동 가능
            ci, cj = ni, nj # 이동
        else: # 범위밖 또는 이미 기록한 위치
            dr = (dr+1)%4 # 방향 꺾기 , 3일 경우 4가 되니깐 4로 나눠준다. 0 1 2 3 반복을 하게 해줌
            ci, cj = ci + di[dr] , cj + dj[dr]
    print(f'{cj} {ci}')